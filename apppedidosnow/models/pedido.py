from django.db import models

from apppedidosnow.models import Produto

class Pedido(models.Model):
    class StatusPedido(models.IntegerChoices):
        PRODUCAO = (
            1,
            "Produção",
        )
        PRONTO = (
            2,
            "Pronto",
        )
        FECHADO = (
            3,
            "Fechado",
        )

        # usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name="pedidos")
        status = models.IntegerField(choices=StatusPedido.choices, default=StatusPedido.PRODUCAO)

        @property
        def total(self):
            return sum(produto.preco_produto * produto.quantidade for produto in self.produtos.all())

        def __str__(self):
            return f"Pedido {self.id} - {self.usuario.nome}"
        
class ItensPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name="+")
    quantidade = models.IntegerField(default=1)
    preco_item = models.DecimalField(max_digits=10, decimal_places=2)