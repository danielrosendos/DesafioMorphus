from rest_framework.serializers import ModelSerializer
from filmeCategoria.models import FilmeCategoria

class FilmeCategoriaSerializer(ModelSerializer):
    class Meta:
        model = FilmeCategoria
        fields = [
            'link', 'title', 'year', 'categories', 'director', 'duration'
        ]