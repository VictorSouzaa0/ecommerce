from django.db import models

class Produto(models.Model):
    tituloProduto = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=255)
    imgProduto = models.CharField(max_length=255)
    categoriaProduto = models.CharField(max_length=255)
    classProduto = models.DecimalField(max_digits=10, decimal_places=2)
    exibirNome = models.BooleanField(default=True)
 