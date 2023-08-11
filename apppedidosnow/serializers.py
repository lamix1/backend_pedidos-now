from rest_framework.serializers import ModelSerializer

from apppedidosnow.models import Categoria, Produto

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"