from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)  # <- existe en el modelo
    url = models.URLField(blank=True, null=True)  # <- pon null=True para evitar el prompt
    image = models.ImageField(upload_to="movie/images/", default="movie/images/default.jpg")
    url = models.URLField(blank=True)
    genre = models.CharField(max_length=100, blank=True)
    year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
