# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0006_auto_20150110_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_num_of_beds',
            field=models.IntegerField(default=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='room',
            name='room_rate',
            field=models.FloatField(default=100),
            preserve_default=True,
        ),
    ]
