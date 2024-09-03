from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtistsViewSet

# Cria um roteador e registra as views
router = DefaultRouter()
router.register(r'artists', ArtistsViewSet, basename='artist')

urlpatterns = [
    path('', include(router.urls)),
]
