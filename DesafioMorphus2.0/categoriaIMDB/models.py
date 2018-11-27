from django.db import models
from django.contrib.auth.models import User

class Categorias(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.CharField(max_length=150)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.categories

