from django.db import models
from artists.models import Artists
from songs.models import Songs

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artists, on_delete=models.CASCADE, related_name='albums')
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='album_covers/', null=True, blank=True)
    isSingle = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
class AlbumSongs(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='tracks')
    song = models.ForeignKey(Songs, on_delete=models.CASCADE, related_name='albums')
    
    def __str__(self):
        return f'{self.song.title} in {self.album.title}'