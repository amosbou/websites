# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0003_auto_20150307_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='guest',
        ),
    ]
