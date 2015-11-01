# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0017_auto_20150412_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='unique_id',
            field=models.CharField(default=1, unique=True, max_length=10),
            preserve_default=False,
        ),
    ]
