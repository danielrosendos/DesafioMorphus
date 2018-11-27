from django.db.models.signals import post_save
from django.db.models import F
from django.dispatch import receiver
from .models import Categorias
from filmeCategoria.models import FilmeCategoria
from filmeCategoria import varreduraDados

def film_categoria(sender, instance, created, **kwargs):
    if created and instance.categories:
        FilmeCategoria.save(varreduraDados.links('Animation'))