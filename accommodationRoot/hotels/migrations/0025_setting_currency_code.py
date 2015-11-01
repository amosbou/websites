# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0024_auto_20150510_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='currency_code',
            field=models.CharField(default='GBP', max_length=12),
            preserve_default=True,
        ),
    ]
