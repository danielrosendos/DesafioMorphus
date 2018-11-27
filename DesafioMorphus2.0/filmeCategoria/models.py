from django.db import models

class FilmeCategoria(models.Model):
    link = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    categories = models.CharField(max_length=255)
    director = models.CharField(max_length=150)
    duration = models.CharField(max_length=150)

    def __str__(self):
        return self.title