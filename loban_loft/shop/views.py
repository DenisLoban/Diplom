from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.views.generic import ListView, DetailView, CreateView
from slugify import slugify

from .forms import UserRegisterForm, LoginForm, ReviewForm, ApplicationModelForm
from .models import Product, Category, Order, OrderItem, About, Application, Profile


class SortList:

    def get_sorts(self):
        return Category.objects.all()


class ProductListView(SortList, ListView):
    template_name = 'shop/men.html'
    model = Product
    paginate_by = 2

    def get_queryset(self):
        return Product.objects.filter(is_published=True)


class ProductDetailView(SortList, DetailView):
    template_name = 'shop/single.html'
    model = Product


class FilterCategoryView(SortList, ListView):
    template_name = 'shop/men.html'

    def get_queryset(self):
        queryset = Product.objects.filter(category__in=self.request.GET.getlist("category"))
        return queryset


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    fields = ['profile_pic', 'bio']
    template_name = 'shop/register.html'
    success_url = reverse_lazy('signin')


class SignInView(LoginView):
    form_class = LoginForm
    template_name = 'shop/login.html'


class CartListView(LoginRequiredMixin, ListView):
    model = OrderItem
    template_name = 'shop/checkout.html'
    context_object_name = 'order_item_list'
    login_url = '/login/'

    def get_queryset(self):
        return self.model.objects.filter(Q(order__is_paid=False) & Q(order__user=self.request.user))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CartListView, self).get_context_data()
        context['total_amount'] = 0
        context['cart_amount'] = len(context[self.context_object_name])
        for product in context[self.context_object_name]:
            context['total_amount'] += product.product.price
        return context


def page_not_found(request, exception):
    print(exception)
    return HttpResponse('<b>404 PAGE NOT FOUND</b>')


class AddReview(View):

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        product = Product.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.product = product
            form.save()
        return redirect(product.get_absolute_url())


class Search(ListView):
    paginate_by = 3
    template_name = 'shop/men.html'

    def get_queryset(self):
        return Product.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context


# class ShowProfilePageView(DetailView):
#     model = User
#     template_name = 'shop/user_profile.html'
#
#     def get_context_data(self, *args, **kwargs):
#         users = Profile.objects.all()
#         context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
#         page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
#         context['page_user'] = page_user
#         return context


class AboutListView(ListView):
    template_name = 'shop/about.html'
    model = About


class ApplicationListView(ListView):
    template_name = 'shop/contact.html'
    model = Application
    http_method_names = ('get', 'post')
    context_object_name = 'application_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ApplicationListView, self).get_context_data()
        context['application_form'] = ApplicationModelForm
        return context

    def post(self, request: HttpRequest):
        data = request.POST.dict()
        data.update(slug=slugify(request.POST.get('number')))
        form = ApplicationModelForm(data)
        if form.is_valid():
            form.save()
        return self.get(request=request)


# class CreateProfilePageView(CreateView):
#     model = Profile
#
#     template_name = 'shop/create_profile.html'
#     fields = ['profile_pic', 'bio']
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)
#
#     success_url = reverse_lazy('logout')
