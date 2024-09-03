from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Songs
from .serializers import UserSerializer, SongsSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SongsViewSet(viewsets.ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer