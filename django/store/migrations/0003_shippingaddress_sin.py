# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_order_ship_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='sin',
            field=models.CharField(max_length=24, null=True, blank=True),
        ),
    ]
