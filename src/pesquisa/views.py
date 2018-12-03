from django.views.generic import ListView

from produtos.models import Produto


class PesquisaProdutoView(ListView):
    template_name = "produtos/lista.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        if query is not None:
            return Produto.objects.filter(name__icontains=query)
        return Produto.objects.none()
