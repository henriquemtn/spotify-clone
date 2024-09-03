from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserViewSet, SongsViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'songs', SongsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]