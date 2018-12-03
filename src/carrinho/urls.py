from django.conf.urls import url

from .views import (
    carrinho_home,
    carrinho_update,
)

urlpatterns = [
    url(r'^$', carrinho_home, name='home'),
    url(r'^update/$', carrinho_update, name='update'),
]
