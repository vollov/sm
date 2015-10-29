# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_order_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='agent_share',
            field=models.DecimalField(null=True, max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='order',
            name='currency_rate',
            field=models.DecimalField(null=True, max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='order',
            name='tax_rate',
            field=models.DecimalField(null=True, max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='productorder',
            name='purchase_price',
            field=models.DecimalField(default=None, max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='productorder',
            name='sell_price',
            field=models.DecimalField(default=None, max_digits=9, decimal_places=2),
        ),
    ]
