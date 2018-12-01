import random
import os
from django.db import models


def get_filename_extension(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    # print(instance)
    # print(filename)
    new_filename = random.randint(1, 3910230292)
    name, ext = get_filename_extension(filename)
    final_filename = f'{new_filename}{ext}'
    return f"produtos/{new_filename}/{final_filename}"


class Produto(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10, default=19.99)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
