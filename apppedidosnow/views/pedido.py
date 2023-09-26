from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from apppedidosnow.models import Pedido
from apppedidosnow.serializers import PedidoSerializer, CriarEditarPedidoSerializer


class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["status"]
    search_fields = ["status"]
    ordering_fields = ["status"]
    # ordering = ["usuario"]

    # def get_queryset(self):
    #     usuario = self.request.user
    #     if usuario.is_superuser:
    #         return Compra.objects.all()
    #     if usuario.groups.filter(name="Administradores"):
    #         return Compra.objects.all()
    #     return Compra.objects.filter(usuario=usuario)

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return PedidoSerializer
        return CriarEditarPedidoSerializer