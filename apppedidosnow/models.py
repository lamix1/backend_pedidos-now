from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)
    def __str__(self):
        return self.descricao

class Produto(models.Model):
    titulo = models.CharField(max_length=255)
    código = models.CharField(max_length=8, null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    gramas = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="produtos"
    )
    def __str__(self):
        return f"{self.titulo}"

