from rest_framework.serializers import ModelSerializer, SlugRelatedField

from apppedidosnow.models import Produto

class ProdutoDetailSerializer(ModelSerializer):

    class Meta:
        model = Produto
        fields = "__all__"
        depth = 1

class ProdutoListSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = ["id", "titulo", "preco"]

class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"