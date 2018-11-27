from rest_framework.serializers import ModelSerializer
from categoriaIMDB.models import Categorias

class CategoriasSerializer(ModelSerializer):
    class Meta:
        model = Categorias
        fields = [
            'id', 'categories'
        ]