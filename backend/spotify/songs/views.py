from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Songs
from .serializers import UserSerializer, SongsSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SongsViewSet(viewsets.ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer

    # Função contabilizando as vezes que a música foi tocada
    def update_played_times(self, request, pk=None):
        song = get_object_or_404(Songs, id=pk)
        song.played_times += 1
        song.save()
        serializer = self.get_serializer(song)
        return Response({'message': 'Played times updated', 'played_times': song.played_times}, status=status.HTTP_200_OK)