from rest_framework import serializers
from .models import Produto
 
 
class ProdutoSerializer (serializers.ModelSerializer):
    class meta:
        model = Produto
        fields = ['id',
            'codigoProduto',
            'tituloProduto',
            'preco',
            'descricao',
            'imagemProduto',
            'categoriaProduto',
            'classProduto',
            'exibirNome',
            ]