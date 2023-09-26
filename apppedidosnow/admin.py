from django.contrib import admin

from .models import Produto, Categoria, Pedido, ItensPedido
# admin.site.register(Pedido)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("descricao",)
    search_fields = ("descricao",)
    list_filter = ("descricao",)
    ordering = ("descricao",)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria")
    search_fields = ("titulo", "categoria__descricao")
    list_filter = (
        "categoria",
    )
    ordering = ("titulo", "categoria")
    list_per_page = 25


class ItensPedidoInline(admin.TabularInline):
    model = ItensPedido


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    inlines = [ItensPedidoInline]