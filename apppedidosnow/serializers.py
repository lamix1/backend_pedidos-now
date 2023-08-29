from rest_framework.serializers import ModelSerializer, CharField

from apppedidosnow.models import Categoria, Produto

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class ProdutoSerializer(ModelSerializer):
    categoria = CharField(source="categoria.descricao", read_only=True)
    class Meta:
        model = Produto
        fields = "__all__"