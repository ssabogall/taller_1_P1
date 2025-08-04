from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='movies/imagenes/')
    url= models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

# Create your models here.
