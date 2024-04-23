from django.shortcuts import render, HttpResponse
from .models import Produtos
from datetime import datetime

def index(request):
    produtos = Produtos.objects.all()
    return render(request, 'pages/index.html', {'produtos':produtos})

def adicionar_produto(request):

    if request.method == "POST":
        nome = request.POST['nome']
        preco = request.POST['preco']
        descricao = request.POST['descricao']
        quantidade = request.POST['quantidade']
        codigo = request.POST['codigo']
        em_estoque = False
        if quantidade > 0:
            em_estoque = True 
        data_criacao = datetime.now()


        return render(request, 'pages/adicionar_produto.html')

    else:
        return render(request, 'pages/adicionar_produto.html')
    


# GET - OBTER DADOS
# POST - ENVIAR DADOS
# PUT - ATUALIZAR DADOS
# PATCH - ATUALIZAÇÃO PARCIAL DE DADOS    