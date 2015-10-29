# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_shippingaddress_sin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productorder',
            name='agent',
        ),
    ]
