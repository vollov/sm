# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20151026_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
    ]
