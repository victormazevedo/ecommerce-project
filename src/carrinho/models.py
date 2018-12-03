from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed

from produtos.models import Produto

User = settings.AUTH_USER_MODEL


class CarrinhoManager(models.Manager):
    def new_or_get(self, request):
        carrinho_id = request.session.get("carrinho_id", None)
        qs = self.get_queryset().filter(id=carrinho_id)
        if qs.count() == 1:
            new_obj = False
            carrinho_obj = qs.first()
            if request.user.is_authenticated() and carrinho_obj.usuario is None:
                carrinho_obj.usuario = request.user
                carrinho_obj.save()
        else:
            carrinho_obj = Carrinho.objects.new(usuario=request.user)
            new_obj = True
            request.session['carrinho_id'] = carrinho_obj.id
        return carrinho_obj, new_obj

    def new(self, usuario=None):
        usuario_obj = None
        if usuario is not None:
            if usuario.is_authenticated():
                usuario_obj = usuario
        return self.model.objects.create(usuario=usuario_obj)  # associando o user logado ao carrinho


class Carrinho(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True)
    produtos = models.ManyToManyField(Produto, blank=True)
    subtotal = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)
    updated = models.DateField(auto_now=True)
    timestamp = models.DateField(auto_now_add=True)

    objects = CarrinhoManager()

    def __str__(self):
        return str(self.id)


def m2m_changed_carrinho_receiver(sender, instance, action, *args, **kwargs): # quando a venda é salva, chamamos este método
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        produtos = instance.produtos.all()
        total = 0
        for item in produtos:
            total += item.price
        if instance.subtotal != total:
            instance.subtotal = total
            instance.save()


m2m_changed.connect(m2m_changed_carrinho_receiver, sender=Carrinho.produtos.through)


def pre_save_carrinho_receiver(sender, instance, *args, **kwargs):
    if instance.subtotal > 0:
        instance.total = instance.subtotal +10
    else:
        instance.total = 0.00


pre_save.connect(pre_save_carrinho_receiver, sender=Carrinho)
