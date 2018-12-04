from django.db import models
from django.db.models.signals import pre_save, post_save

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

    def update_total(self):
        total_carrinho = self.carrinho.total
        valor_entrega = self.valor_entrega
        novo_total = total_carrinho + valor_entrega
        self.total = novo_total
        self.save()
        return novo_total


def pre_save_create_id_pedido(sender, instance, *args, **kwargs):
    if not instance.id_pedido:
        instance.id_pedido = unique_id_pedido_generator(instance)


pre_save.connect(pre_save_create_id_pedido, sender=Pedido)


def post_save_total_carrinho(sender, instance, created, *args, **kwargs):
    if not created:
        carrinho_obj = instance
        total_carrinho = carrinho_obj.total
        id_carrinho = carrinho_obj.id
        qs = Pedido.objects.filter(carrinho_id=id_carrinho)
        if qs.count() == 1:
            pedido_obj = qs.first()
            pedido_obj.update_total()

post_save.connect(post_save_total_carrinho, sender=Carrinho)


def post_save_pedido(sender, instance, created, *args, **kwargs):
    if created:
        instance.update_total()

post_save.connect(post_save_pedido, sender=Pedido)