# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import photo.models
import photo.storage
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0003_shippingaddress_sin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=64, serialize=False, verbose_name='Activation key', primary_key=True)),
                ('name', models.CharField(max_length=60, null=True, blank=True)),
                ('weight', models.IntegerField(default=0)),
                ('image', models.ImageField(storage=photo.storage.OverwriteStorage(), upload_to=photo.models.image_upload_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('is_thumbnail', models.BooleanField(default=False)),
                ('product', models.ForeignKey(to='store.Product', null=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
