from rest_framework import viewsets
from .models import Album, AlbumSongs
from .serializers import AlbumSerializer, AlbumSongsSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumSongsViewSet(viewsets.ModelViewSet):
    queryset = AlbumSongs.objects.all()
    serializer_class = AlbumSongsSerializer
