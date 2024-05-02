from django.shortcuts import render, redirect
from .models import Categoria, Produtos
from datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='login')
def index(request):
    produtos = Produtos.objects.all()
    return render(request, 'pages/index.html', {'produtos':produtos})

def adicionar_produto(request):
    if request.method == "POST":
        nome = request.POST['nome']
        preco = request.POST['preco']
        descricao = request.POST['descricao']
        quantidade = request.POST['quantidade']
        categoria = request.POST['categoria']
        codigo = request.POST['codigo']
        em_estoque = False
        if int(quantidade) > 0:
            em_estoque = True 
        data_criacao = datetime.now()

        Produtos.objects.create(
            nome=nome,
            categoria_id =categoria,
            preco=preco,
            descricao=descricao,
            quantidade=quantidade,
            codigo=codigo,
            em_estoque=em_estoque,
            data_criacao=data_criacao
        )
        
        
        return redirect('index')

    else:
        categorias = Categoria.objects.all()
        return render(request, 'pages/adicionar_produto.html', {'categorias':categorias})
    

def produto(request, id):
    detalhe = Produtos.objects.get(id=id) 
    return render(request, 'pages/produto.html', {'detalhe':detalhe})

def excluir(request, id):
    produto = Produtos.objects.get(id=id)
    produto.delete() 
    return redirect('index')
