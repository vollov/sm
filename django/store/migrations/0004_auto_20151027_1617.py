# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_store_agent_share'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storeenrollment',
            name='agent',
        ),
        migrations.RemoveField(
            model_name='storeenrollment',
            name='store',
        ),
        migrations.RemoveField(
            model_name='store',
            name='currency_type',
        ),
        migrations.RemoveField(
            model_name='store',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='store',
            name='sales',
        ),
        migrations.AddField(
            model_name='store',
            name='code',
            field=models.CharField(max_length=10, unique=True, null=True),
        ),
        migrations.DeleteModel(
            name='StoreEnrollment',
        ),
    ]
