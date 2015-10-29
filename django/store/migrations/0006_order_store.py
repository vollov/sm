# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20151029_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='store',
            field=models.ForeignKey(to='store.Store', null=True),
        ),
    ]
