# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image.models
import image.storage
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60, null=True, blank=True)),
                ('image_key', models.CharField(default=uuid.uuid4, max_length=64, verbose_name='Activation key')),
                ('image', models.ImageField(storage=image.storage.OverwriteStorage(), upload_to=image.models.image_upload_path)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('album', models.ForeignKey(to='image.Album')),
            ],
        ),
    ]
