from rest_framework import serializers
from rest_framework.serializers import CharField, ModelSerializer, SerializerMethodField

from apppedidosnow.models import Pedido, ItensPedido, Produto


class ItensPedidoSerializer(ModelSerializer):
    total = SerializerMethodField()

    class Meta:
        model = ItensPedido
        fields = ("quantidade", "preco_item", "total", "produto")
        depth = 2

    def get_total(self, instance):
        return instance.quantidade * instance.preco_item


class PedidoSerializer(ModelSerializer):
    status = CharField(source="get_status_display", read_only=True)
    itens = ItensPedidoSerializer(many=True, read_only=True)

    class Meta:
        model = Pedido
        fields = ("id", "cliente", "mesa", "status", "total", "itens")


class CriarEditarItensPedidoSerializer(ModelSerializer):
    class Meta:
        model = ItensPedido
        fields = ("produto")

    def validate(self, data):
         return data


class CriarEditarPedidoSerializer(ModelSerializer):
    itens = serializers.ListField(child = serializers.IntegerField(), write_only=True)

    class Meta:
        model = Pedido
        fields = ("cliente", "mesa", "itens")

    def create(self, validated_data):
        itens = validated_data.pop("itens")
        pedido = Pedido.objects.create(**validated_data)
        for item in itens:
            print(item)
            produto = Produto.objects.get(id=item)
            preco_item = produto.preco
            quantidade = produto.quantidade
            ItensPedido.objects.create(pedido=pedido, produto=produto, preco_item=preco_item, quantidade=quantidade)
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