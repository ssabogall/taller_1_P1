from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='movies/imagenes/')
    url= models.URLField(blank=True, null=True)
    genre = models.CharField(blank=True, max_length=250)
    year = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.title

