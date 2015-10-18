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
            name='currency_rate',
            field=models.DecimalField(default=5, max_digits=9, decimal_places=4),
        ),
        migrations.AddField(
            model_name='store',
            name='currency_type',
            field=models.CharField(default=b'CAD', max_length=3, null=True),
        ),
    ]
