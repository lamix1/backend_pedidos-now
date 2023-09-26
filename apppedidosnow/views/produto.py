from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from apppedidosnow.models import Produto
from apppedidosnow.serializers import (
    ProdutoDetailSerializer,
    ProdutoListSerializer,
    ProdutoSerializer,
)


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["categoria__descricao"]
    search_fields = ["titulo"]
    ordering_fields = ["titulo", "preco"]
    ordering = ["titulo"]

    def get_serializer_class(self):
        if self.action == "list":
            return ProdutoListSerializer
        elif self.action == "retrieve":
            return ProdutoDetailSerializer
        else:
            return ProdutoSerializer