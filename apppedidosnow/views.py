from rest_framework.viewsets import ModelViewSet

from apppedidosnow.models import Categoria, Produto
from apppedidosnow.serializers import CategoriaSerializer, ProdutoSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer