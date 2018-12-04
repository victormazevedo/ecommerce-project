from django.conf.urls import url
from .views import export_produtos

from .views import (
    ProdutoListView,
    ProdutoDetailSlugView)

urlpatterns = [
    url(r'^$', ProdutoListView.as_view(), name='lista'),
    url(r'^(?P<slug>[\w-]+)/$', ProdutoDetailSlugView.as_view(), name='detalhe'),
    url(r'^export_produtos', export_produtos, name='export_produtos'),
]
