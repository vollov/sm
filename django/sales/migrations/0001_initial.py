# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=64, serialize=False, verbose_name='Activation key', primary_key=True)),
                ('name', models.CharField(max_length=16, null=True, blank=True)),
                ('sin', models.CharField(max_length=24, null=True, blank=True)),
                ('address', models.CharField(max_length=125, null=True, blank=True)),
                ('phone', models.CharField(max_length=10, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('agent', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=64, serialize=False, verbose_name='Activation key', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('delivery_cost', models.DecimalField(default=0, max_digits=9, decimal_places=4)),
                ('status', models.CharField(default=b'Y', max_length=2, choices=[(b'F', b'Closed'), (b'S', b'Shipping'), (b'Y', b'Confirmed'), (b'X', b'Cancel')])),
                ('agent', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
                ('store', models.ForeignKey(to='store.Store', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=64, serialize=False, verbose_name='Activation key', primary_key=True)),
                ('name', models.CharField(max_length=60, null=True, blank=True)),
                ('code', models.CharField(max_length=8, null=True, blank=True)),
                ('purchase_price', models.DecimalField(max_digits=9, decimal_places=4)),
                ('sell_price', models.DecimalField(max_digits=9, decimal_places=4)),
                ('market_price', models.DecimalField(max_digits=9, decimal_places=4)),
                ('desc', models.CharField(max_length=125, null=True, blank=True)),
                ('note', models.CharField(max_length=125, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('store', models.ForeignKey(to='store.Store', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=64, serialize=False, verbose_name='Activation key', primary_key=True)),
                ('amount', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('agent', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
                ('customer', models.ForeignKey(to='sales.Customer', null=True)),
                ('order', models.ForeignKey(to='sales.Order', null=True)),
                ('product', models.ForeignKey(to='sales.Product', null=True)),
                ('store', models.ForeignKey(to='store.Store', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='product_orders',
            field=models.ManyToManyField(related_name='product_orders', through='sales.ProductOrder', to='sales.Product'),
        ),
        migrations.AddField(
            model_name='customer',
            name='store',
            field=models.ForeignKey(to='store.Store', null=True),
        ),
    ]
