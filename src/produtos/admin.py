from django.contrib import admin

from .models import Produto


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']

    class Meta:
        model = Produto


admin.site.register(Produto, ProdutoAdmin)
