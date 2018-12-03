from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404


from .models import Produto


class ProdutoFeaturedListView(ListView):
    template_name = "produtos/lista.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Produto.objects.all().featured()


class ProdutoFeaturedDetailView(DetailView):
    queryset = Produto.objects.all().featured()
    template_name = "produtos/featured-detail.html"

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Produto.objects.featured()


class ProdutoListView(ListView):
    template_name = "produtos/lista.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProdutoListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Produto.objects.all()


def produto_list_view(request):
    queryset = Produto.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "produtos/lista.html", context)


class ProdutoDetailSlugView(DetailView):
    queryset = Produto.objects.all()
    template_name = "produtos/detalhe.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = get_object_or_404(Produto, slug=slug, active=True)
        # aqui estamos definindo caso retorne multiplos objetos, pegamos o primeiro
        try:
            instance = Produto.objects.get(slug=slug, active=True)
        except Produto.DoesNotExist:
            raise Http404("Produto não encontado!")
        except Produto.MultipleObjectsReturned:
            qs = Produto.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Teste do Joselito")
        return instance


class ProdutoDetailView(DetailView):
    # queryset = Produto.objects.all()
    template_name = "produtos/detalhe.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProdutoDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Produto.objects.get_by_id(pk)
        if instance is None:
            raise Http404("O produto não existe!")
        return instance


def produto_detail_view(request, pk=None, *args, **kwargs):
    # # instance = Produto.objects.get(pk=pk)
    # # instance = get_object_or_404(Produto, pk=pk)
    # try:
    #     instance = Produto.objects.get(id=pk)
    # except Produto.DoesNotExist:
    #     print("Produto não encontrado!")
    #     raise Http404("O produto não existe!")
    # except:
    #     print("q?")
    instance = Produto.objects.get_by_id(pk)
    if instance is None:
        raise Http404("O produto não existe!")
    # print(instance)
    # qs = Produto.objects.filter(id=pk)
    # if qs.exists() and qs.count() == 1:
    #     instance = qs.first()
    # else:
    #     raise Http404("O produto não existe!")

    context = {
        'object': instance
    }
    return render(request, "produtos/detalhe.html", context)
