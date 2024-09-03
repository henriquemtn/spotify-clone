from rest_framework import serializers
from .models import Artists
from songs.serializers import SongsSerializer

# Serializer para Artists
class ArtistsSerializer(serializers.ModelSerializer):
    songs = SongsSerializer(many=True, read_only=True)  # Relaciona as músicas ao artista

    class Meta:
        model = Artists
        fields = ['id', 'name', 'banner', 'isVerified', 'songs', 'genre']
