#  classe usada para mapear o banco de dados, no caso está sendo utilizado o sqlite, integrado ao django
#  versão do Django 1.11
import random
import os
from django.db import models


def get_filename_extension(filename):  # usado para pegar a extensão da img que foi upada
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):  # usado para modificar o path da img a ser upada
    new_filename = random.randint(1, 3910230292)
    name, ext = get_filename_extension(filename)
    final_filename = f'{new_filename}{ext}'
    return f"produtos/{new_filename}/{final_filename}"


class ProdutoQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)


class ProdutoManager(models.Manager):
    def get_queryset(self):
        return ProdutoQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self):
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None


class Produto(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10, default=19.99)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    objects = ProdutoManager()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
