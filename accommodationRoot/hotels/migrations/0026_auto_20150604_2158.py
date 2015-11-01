# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0025_setting_currency_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='phone_number',
            field=models.CharField(default='', max_length=50),
        ),
    ]
