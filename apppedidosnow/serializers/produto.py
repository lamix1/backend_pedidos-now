from rest_framework.serializers import ModelSerializer, SlugRelatedField, CharField

from apppedidosnow.models import Produto

class ProdutoDetailSerializer(ModelSerializer):

    class Meta:
        model = Produto
        fields = "__all__"
        depth = 1

class ProdutoListSerializer(ModelSerializer):
    categoria = CharField(source="categoria.descricao")
    class Meta:
        model = Produto
        fields = ["id", "titulo", "preco", "categoria"]

class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"