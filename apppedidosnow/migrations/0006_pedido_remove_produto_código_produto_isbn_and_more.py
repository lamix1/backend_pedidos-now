# Generated by Django 4.2.4 on 2023-09-27 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("apppedidosnow", "0005_alter_produto_código"),
    ]

    operations = [
        migrations.CreateModel(
            name="Pedido",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[(1, "PRODUCAO"), (2, "PRONTO"), (3, "Pago")], default=1
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="produto",
            name="código",
        ),
        migrations.AddField(
            model_name="produto",
            name="isbn",
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name="produto",
            name="quantidade",
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.CreateModel(
            name="ItensPedido",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantidade", models.IntegerField(default=1)),
                ("preco_item", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "pedido",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="itens",
                        to="apppedidosnow.pedido",
                    ),
                ),
                (
                    "produto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="apppedidosnow.produto",
                    ),
                ),
            ],
        ),
    ]
