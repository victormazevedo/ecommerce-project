from django.db import models
from django.db.models.signals import pre_save


from carrinho.models import Carrinho
from ecommerce.utils import unique_id_pedido_generator

STATUS_PEDIDO = (
    ('realizado', 'Realizado'),
    ('pago', 'Pago'),
    ('preparo', 'Em preparo'),
    ('entrega', 'Saiu para entrega'),
)

class Pedido(models.Model):
    id_pedido = models.CharField(max_length=120, blank=True)
    carrinho = models.ForeignKey(Carrinho)
    status = models.CharField(max_length=120, default='criado')
    valor_entrega = models.DecimalField(default=8.00, max_digits=20, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)

    def __str__(self):
        return self.id_pedido


def pre_save_create_id_pedido(sender, instance, *args, **kwargs):
    if not instance.id_pedido:
        instance.id_pedido = unique_id_pedido_generator(instance)


pre_save.connect(pre_save_create_id_pedido, sender=Pedido)

