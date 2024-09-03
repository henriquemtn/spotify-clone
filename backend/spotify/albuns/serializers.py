from rest_framework import serializers
from .models import Album, AlbumSongs
from songs.serializers import SongsSerializer
from artists.models import Artists 

class AlbumSerializer(serializers.ModelSerializer):
    artist = serializers.PrimaryKeyRelatedField(queryset=Artists.objects.all())

    class Meta:
        model = Album
        fields = ['id', 'title', 'artist', 'release_date', 'cover_image', 'isSingle']

class AlbumSongsSerializer(serializers.ModelSerializer):
    song = SongsSerializer()

    class Meta:
        model = AlbumSongs
        fields = ['id', 'album', 'song']
