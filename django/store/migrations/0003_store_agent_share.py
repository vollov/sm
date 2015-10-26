# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_store_tax_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='agent_share',
            field=models.DecimalField(default=0.4, max_digits=9, decimal_places=4),
        ),
    ]
