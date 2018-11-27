from django.apps import AppConfig
from django.db.models.signals import post_save

class CategoriaimdbConfig(AppConfig):
    name = 'categoriaIMDB'

    def ready(self):
        from .models import Categorias
        from .signals import film_categoria
        post_save.connect(film_categoria, sender=Categorias)
