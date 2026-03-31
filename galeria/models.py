from django.db import models

class Imagen(models.Model):
    titulo = models.CharField(max_length=100)
    archivo = models.ImageField(upload_to='fotos/')
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo