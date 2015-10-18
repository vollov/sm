# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import photo.models
import photo.storage
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20151017_1733'),
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='is_thumbnail',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(max_length=60, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='image',
            name='product',
            field=models.ForeignKey(to='sales.Product', null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.CharField(default=uuid.uuid4, max_length=64, serialize=False, verbose_name='Activation key', primary_key=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(storage=photo.storage.OverwriteStorage(), upload_to=photo.models.image_upload_path),
        ),
    ]
