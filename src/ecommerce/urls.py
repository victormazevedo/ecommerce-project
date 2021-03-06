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

from .views import home_page, about_page, contact_page, login_page, register_page

urlpatterns = [
    url(r'^$', home_page, name='home'),
    url(r'^sobre/$', about_page, name='about'),
    url(r'^contato/$', contact_page, name='contact'),
    url(r'^login/$', login_page),
    url(r'^registro/$', register_page, name='register'),
    url(r'^carrinho/', include("carrinho.urls", namespace='carrinho')),
    url(r'^registro/$', register_page),
    url(r'^produtos/', include("produtos.urls", namespace='produtos')),
    url(r'^pesquisa/', include("pesquisa.urls", namespace='pesquisa')),
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'^avisos/', include("clima.urls", namespace='clima')),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
