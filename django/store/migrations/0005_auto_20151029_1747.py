# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_productorder_agent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productorder',
            name='purchase_price',
            field=models.DecimalField(default=0, max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='productorder',
            name='sell_price',
            field=models.DecimalField(default=0, max_digits=9, decimal_places=2),
        ),
    ]
