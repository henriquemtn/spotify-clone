from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Songs

# Serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
        
# Serializer para Songs
class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ['id', 'title', 'artist', 'audio_file', 'played_times']
        extra_kwargs = {
            'artist': {'required': True},
        }