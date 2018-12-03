from django.shortcuts import render, redirect

from produtos.models import Produto
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
