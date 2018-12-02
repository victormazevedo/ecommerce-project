from django.conf.urls import url

from .views import (
    ProdutoListView,
    ProdutoDetailSlugView,
)

urlpatterns = [
    url(r'^$', ProdutoListView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', ProdutoDetailSlugView.as_view()),
]
