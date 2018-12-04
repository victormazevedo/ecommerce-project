# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-04 01:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carrinho', '0002_carrinho_subtotal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pedido', models.CharField(blank=True, max_length=120)),
                ('status', models.CharField(default='criado', max_length=120)),
                ('valor_entrega', models.DecimalField(decimal_places=2, default=8.0, max_digits=20)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('carrinho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrinho.Carrinho')),
            ],
        ),
    ]
