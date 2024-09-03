from rest_framework import viewsets
from .models import Artists
from songs.models import Songs
from .serializers import ArtistsSerializer

# ViewSet para Artists
class ArtistsViewSet(viewsets.ModelViewSet):
    queryset = Artists.objects.all()
    serializer_class = ArtistsSerializer