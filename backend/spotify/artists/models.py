from django.db import models

# Modelo dos Artistas
class Artists(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    banner = models.FileField(upload_to='artists_images/', blank=True, null=True)
    isVerified = models.BooleanField(default=False)
    genre = models.CharField(max_length=20, default='Indefinido')

    def __str__(self):
        return self.name

    def get_songs(self):
        return self.songs_set.all()  # Retorna todas as músicas associadas a este artista utilizando um Foreign Key
