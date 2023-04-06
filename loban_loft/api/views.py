from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from slugify import slugify
from .serializers import CategorySerializer, CalculatorSerializer
from rest_framework.viewsets import ModelViewSet, ViewSet
from shop.models import Category
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, BasePermission, SAFE_METHODS
from rest_framework.pagination import PageNumberPagination


class IsAdminUserOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and request.user.is_staff
        )


class CategoryModelViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminUserOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.POST.dict() | {'slug': slugify(request.data.get('name'))})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance,
                                         data=request.data.dict() | {'slug': slugify(request.data.get('name'))},
                                         partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
