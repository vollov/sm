# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
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
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=64, serialize=False, verbose_name='Activation key', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default=b'W', max_length=2, choices=[(b'F', b'Automatic'), (b'P', b'Manual'), (b'W', b'Waiting Confirm'), (b'C', b'Cancel')])),
                ('customer', models.ForeignKey(to='sales.Customer')),
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
            ],
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=64, serialize=False, verbose_name='Activation key', primary_key=True)),
                ('amount', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('customers', models.ManyToManyField(to='sales.Customer', through='sales.Order')),
                ('product', models.ForeignKey(to='sales.Product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='product_order',
            field=models.ForeignKey(to='sales.ProductOrder'),
        ),
    ]
