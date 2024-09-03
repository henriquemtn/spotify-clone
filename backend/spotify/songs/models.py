from django.db import models
from django.core.exceptions import ValidationError
import os

from artists.models import Artists  # Importando o modelo de Artistas

def validate_audio_file(value):
    valid_extensions = ['.mp3', '.wav', '.ogg', '.flac']  # Adicione outras extensões conforme necessário
    ext = os.path.splitext(value.name)[1]  # Obtém a extensão do arquivo
    if ext.lower() not in valid_extensions:
        raise ValidationError(f'Unsupported file extension. Allowed extensions are: {", ".join(valid_extensions)}.')
    
# Modelo das Músicas
class Songs(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artists, on_delete=models.CASCADE, related_name='songs')  # Chave estrangeira para Artists
    audio_file = models.FileField(upload_to='audio/', validators=[validate_audio_file])


    def __str__(self):
        return self.title