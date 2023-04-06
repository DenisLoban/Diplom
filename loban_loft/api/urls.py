from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import CategoryModelViewSet

router = SimpleRouter()
router.register('category', CategoryModelViewSet)

urlpatterns = [
    path('v1/', include(router.urls))
]