from django.conf.urls import url

from .views import (
    carrinho_home,
    carrinho_update,
    checkout_home,
)

urlpatterns = [
    url(r'^$', carrinho_home, name='home'),
    url(r'^checkout/$', checkout_home, name='checkout'),
    url(r'^update/$', carrinho_update, name='update'),
]
