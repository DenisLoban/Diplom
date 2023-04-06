from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import *

urlpatterns = [

    path('', ProductListView.as_view(), name='shop_product_list'),
    path('category/', FilterCategoryView.as_view(), name='category'),
    path('contact/', ApplicationListView.as_view(), name='contact'),
    path('register/', RegisterView.as_view(), name='signup'),
    path('login/', SignInView.as_view(), name='signin'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('cart/', CartListView.as_view(), name='shop_cart'),
    path('search/', Search.as_view(), name='search'),
    path('about/', AboutListView.as_view(), name='about'),

    path('<slug:slug>/', ProductDetailView.as_view(), name='shop_product_detail'),
    path('review/<int:pk>/', AddReview.as_view(), name='add_review'),
    # path('user_profile/<int:pk>/', ShowProfilePageView.as_view(), name='user_profile'),

]
