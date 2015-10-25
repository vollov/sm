# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='tax_rate',
            field=models.DecimalField(default=0.13, max_digits=9, decimal_places=4),
        ),
    ]
