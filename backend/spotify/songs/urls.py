from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserViewSet, SongsViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'songs', SongsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('songs/<int:pk>/increment_played_times/', SongsViewSet.as_view({'post': 'update_played_times'}), name='increment_played_times'),
]