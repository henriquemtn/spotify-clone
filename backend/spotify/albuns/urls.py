from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlbumViewSet, AlbumSongsViewSet

router = DefaultRouter()
router.register(r'albums', AlbumViewSet)
router.register(r'album-songs', AlbumSongsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
