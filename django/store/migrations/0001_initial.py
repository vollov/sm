# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('phone', models.CharField(max_length=16)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'agents',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=64, serialize=False, verbose_name='Activation key', primary_key=True)),
                ('name', models.CharField(max_length=16, null=True, blank=True)),
                ('sin', models.CharField(max_length=24, null=True, blank=True)),
                ('address', models.CharField(max_length=125, null=True, blank=True)),
                ('phone', models.CharField(max_length=16, null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('agent', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=64, serialize=False, verbose_name='Activation key', primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('delivery_company', models.CharField(max_length=255, null=True, blank=True)),
                ('tarcking_code', models.CharField(max_length=255, null=True, blank=True)),
                ('delivery_cost', models.DecimalField(default=0.0, max_digits=9, decimal_places=3)),
                ('status', models.CharField(default=b'Y', max_length=2, choices=[(b'F', b'Closed'), (b'S', b'Shipping'), (b'Y', b'Confirmed'), (b'X', b'Cancel')])),
                ('currency_rate', models.DecimalField(default=5.5, max_digits=9, decimal_places=2)),
                ('tax_rate', models.DecimalField(default=0.13, max_digits=9, decimal_places=2)),
                ('agent_share', models.DecimalField(default=0.4, max_digits=9, decimal_places=2)),
                ('agent', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=64, serialize=False, verbose_name='Activation key', primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('sku', models.CharField(unique=True, max_length=64)),
                ('purchase_price', models.DecimalField(max_digits=9, decimal_places=2)),
                ('sell_price', models.DecimalField(max_digits=9, decimal_places=2)),
                ('market_price', models.DecimalField(max_digits=9, decimal_places=2)),
                ('desc', models.TextField(null=True, blank=True)),
                ('note', models.CharField(max_length=125, null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=64, serialize=False, verbose_name='Activation key', primary_key=True)),
                ('quantity', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sell_price', models.DecimalField(default=0, max_digits=9, decimal_places=4)),
                ('purchase_price', models.DecimalField(default=0, max_digits=9, decimal_places=4)),
                ('agent', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
                ('customer', models.ForeignKey(to='store.Customer', null=True)),
                ('order', models.ForeignKey(to='store.Order', null=True)),
                ('product', models.ForeignKey(to='store.Product', null=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'product_orders',
            },
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=64, serialize=False, verbose_name='Activation key', primary_key=True)),
                ('name', models.CharField(unique=True, max_length=16)),
                ('phone', models.CharField(max_length=16, null=True, blank=True)),
                ('address', models.CharField(max_length=50, blank=True)),
                ('postcode', models.CharField(max_length=10, null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('agent', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'shipping_address',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=64, serialize=False, verbose_name='Activation key', primary_key=True)),
                ('name', models.CharField(max_length=60, unique=True, null=True)),
                ('code', models.CharField(max_length=10, unique=True, null=True)),
                ('currency_rate', models.DecimalField(default=5.5, max_digits=9, decimal_places=2)),
                ('tax_rate', models.DecimalField(default=0.13, max_digits=9, decimal_places=2)),
                ('agent_share', models.DecimalField(default=0.4, max_digits=9, decimal_places=2)),
                ('meta_keywords', models.CharField(max_length=255, null=True, blank=True)),
                ('meta_description', models.CharField(max_length=255, null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'stores',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='product_orders',
            field=models.ManyToManyField(related_name='product_orders', through='store.ProductOrder', to='store.Product'),
        ),
    ]
