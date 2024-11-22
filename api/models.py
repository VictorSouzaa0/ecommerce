from django.db import models

class Produto(models.Model):
    tituloProduto = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=255)
    imgProduto = models.CharField(max_length=255)
    catProduto = models.CharField(max_length=255)
    classProduto = models.CharField(max_length=255)
    exibirNome = models.BooleanField(default=True)
 