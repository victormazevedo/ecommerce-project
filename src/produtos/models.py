from django.db import models

# Create your models here.


class Produto(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10, default=19.99)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
