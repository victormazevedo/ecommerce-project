from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404


from .models import Produto


class ProdutoListView(ListView):
    queryset = Produto.objects.all()
    template_name = "produtos/lista.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProdutoListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context


def produto_list_view(request):
    queryset = Produto.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "produtos/lista.html", context)


class ProdutoDetailView(DetailView):
    queryset = Produto.objects.all()
    template_name = "produtos/detalhe.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProdutoDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context


def produto_detail_view(request, pk=None, *args, **kwargs):
    # instance = Produto.objects.get(pk=pk)
    instance = get_object_or_404(Produto, pk=pk)
    context = {
        'object': instance
    }
    return render(request, "produtos/detalhe.html", context)
