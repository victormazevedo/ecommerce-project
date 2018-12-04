from django.shortcuts import render, redirect

from produtos.models import Produto
from pedidos.models import Pedido
from .models import Carrinho


def carrinho_home(request):
    carrinho_obj, new_obj = Carrinho.objects.new_or_get(request)
    return render(request, "carrinho/home.html", {"carrinho": carrinho_obj})


def carrinho_update(request):
    produto_id = request.POST.get('produtos_id')
    if produto_id is not None:
        try:
            produto_obj = Produto.objects.get(id=produto_id)
        except Produto.DoesNotExist:
            return redirect("carrinho:home")
        carrinho_obj, new_obj = Carrinho.objects.new_or_get(request)
        if produto_obj in carrinho_obj.produtos.all():
            carrinho_obj.produtos.remove(produto_obj)
        else:
            carrinho_obj.produtos.add(produto_obj)
        request.session['total_itens'] = carrinho_obj.produtos.count()
    return redirect("carrinho:home")


def checkout_home(request):
    carrinho_obj, carrinho_criado = Carrinho.objects.new_or_get(request)
    pedidos_obj = None

    if carrinho_criado or carrinho_obj.produtos.count() == 0:
        return redirect("carrinho:home")
    else:
        pedidos_obj, novo_pedido = Pedido.objects.get_or_create(carrinho=carrinho_obj)
    return render(request, "carrinho/checkout.html", {"object": pedidos_obj})

