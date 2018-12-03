"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.conf import settings
from django.contrib.auth.views import logout
from django.contrib import admin


# from produtos.views import (
#     ProdutoListView,
#     produto_list_view,
#     ProdutoDetailView,
#     ProdutoDetailSlugView,
#     produto_detail_view,
#     ProdutoFeaturedListView,
#     ProdutoFeaturedDetailView
# )

from .views import home_page, about_page, contact_page, login_page, register_page

urlpatterns = [
    url(r'^$', home_page, name='home'),
    url(r'^sobre/$', about_page, name='about'),
    url(r'^contato/$', contact_page, name='contact'),
    url(r'^login/$', login_page),
    url(r'^registro/$', register_page, name='register'),
    url(r'^produtos/', include("produtos.urls", namespace='produtos')),
    url(r'^pesquisa/', include("pesquisa.urls", namespace='pesquisa')),
    # url(r'^featured/$', ProdutoFeaturedListView.as_view()),
    # url(r'^featured/(?P<pk>\d+)/$', ProdutoFeaturedDetailView.as_view()),
    # url(r'^produtos/$', ProdutoListView.as_view()),
    # url(r'^produtos-fbv/$', produto_list_view),
    # # url(r'^produtos/(?P<pk>\d+)/$', ProdutoDetailView.as_view()),
    # url(r'^produtos/(?P<slug>[\w-]+)/$', ProdutoDetailSlugView.as_view()),
    # url(r'^produtos-fbv/(?P<pk>\d+)/$', produto_detail_view),
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout')
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
