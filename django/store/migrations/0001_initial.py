# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=64, serialize=False, verbose_name='Activation key', primary_key=True)),
                ('name', models.CharField(max_length=60, unique=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StoreEnrollment',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=64, serialize=False, verbose_name='Activation key', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('agent', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('store', models.ForeignKey(to='store.Store')),
            ],
        ),
        migrations.AddField(
            model_name='store',
            name='sales',
            field=models.ManyToManyField(related_name='sales', through='store.StoreEnrollment', to=settings.AUTH_USER_MODEL),
        ),
    ]
