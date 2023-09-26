from rest_framework import serializers
from rest_framework.serializers import CharField, ModelSerializer, SerializerMethodField

from apppedidosnow.models import Pedido, ItensPedido


class ItensPedidoSerializer(ModelSerializer):
    total = SerializerMethodField()

    class Meta:
        model = ItensPedido
        fields = ("quantidade", "preco_item", "total", "produto")
        depth = 2

    def get_total(self, instance):
        return instance.quantidade * instance.preco_item


class PedidoSerializer(ModelSerializer):
    # usuario = CharField(source="usuario.email", read_only=True)
    status = CharField(source="get_status_display", read_only=True)
    # data = serializers.DateTimeField(read_only=True)
    itens = ItensPedidoSerializer(many=True, read_only=True)

    class Meta:
        model = Pedido
        fields = ("id", "status", "total", "itens")


class CriarEditarItensPedidoSerializer(ModelSerializer):
    class Meta:
        model = ItensPedido
        fields = ("produto", "quantidade")

    def validate(self, data):
         if data["quantidade"] > data["produto"].quantidade:
             raise serializers.ValidationError({"quantidade": "Quantidade solicitada não disponível em estoque."})
         return data


class CriarEditarPedidoSerializer(ModelSerializer):
    itens = CriarEditarItensPedidoSerializer(many=True)
    # usuario = serializers.HiddenField(default=serializers.CurrentUserDefault())
    data = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Pedido
        fields = ("data", "itens")

    def create(self, validated_data):
        itens = validated_data.pop("itens")
        pedido = Pedido.objects.create(**validated_data)
        for item in itens:
            item["preco_item"] = item["produto"].preco  # Coloquem o preço do produto no item de compra
            ItensPedido.objects.create(pedido=pedido, **item)
        pedido.save()
        return pedido

    def update(self, instance, validated_data):
        itens = validated_data.pop("itens")
        if itens:
            instance.itens.all().delete()
            for item in itens:
                ItensPedido.objects.create(pedido=instance, **item)
        instance.save()
        return instance