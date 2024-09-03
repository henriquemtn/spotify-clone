from rest_framework import serializers
from .models import Artists
from albuns.models import Album
from songs.serializers import SongsSerializer

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id']  # Only include the ID in this serializer

# Serializer para Artists
class ArtistsSerializer(serializers.ModelSerializer):
    songs = SongsSerializer(many=True, read_only=True)  # Relaciona as músicas ao artista
    album_ids = serializers.SerializerMethodField() 

    class Meta:
        model = Artists
        fields = ['id', 'name', 'banner', 'isVerified', 'songs', 'genre', 'album_ids']
        
    def get_album_ids(self, obj):
        # Return a list of album IDs associated with this artist
        return obj.albums.values_list('id', flat=True)
