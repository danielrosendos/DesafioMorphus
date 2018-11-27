from rest_framework.viewsets import ModelViewSet
from categoriaIMDB.models import Categorias
from .serializers import CategoriasSerializer

class CategoriasViewSet(ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer