from rest_framework.viewsets import ModelViewSet
from filmeCategoria.models import FilmeCategoria
from .serializers import FilmeCategoriaSerializer

class FilmeCategoriaViewSet(ModelViewSet):
    queryset = FilmeCategoria.objects.all()
    serializer_class = FilmeCategoriaSerializer