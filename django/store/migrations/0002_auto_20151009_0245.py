# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AlterField(
            model_name='store',
            name='owner',
            field=models.ForeignKey(to='account.UserProfile'),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
