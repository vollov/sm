# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20151017_1633'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='agent',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='store',
            field=models.ForeignKey(to='store.Store', null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='agent',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='store',
            field=models.ForeignKey(to='store.Store', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='store',
            field=models.ForeignKey(to='store.Store', null=True),
        ),
        migrations.AddField(
            model_name='productorder',
            name='agent',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='productorder',
            name='store',
            field=models.ForeignKey(to='store.Store', null=True),
        ),
    ]
