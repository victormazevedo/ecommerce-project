# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-03 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrinho', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrinho',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
    ]
