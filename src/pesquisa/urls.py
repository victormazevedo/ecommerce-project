from django.conf.urls import url

from .views import (
    PesquisaProdutoView,
)

urlpatterns = [
    url(r'^$', PesquisaProdutoView.as_view(), name='query'),
]
