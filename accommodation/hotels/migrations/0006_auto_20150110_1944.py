# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0005_calendar_calendar_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_caption',
            field=models.CharField(default=b'unset', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room',
            name='room_num_of_beds',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='room_rate',
            field=models.FloatField(default=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='calendar',
            name='calendar_name',
            field=models.CharField(default=b'unset', max_length=200),
            preserve_default=True,
        ),
    ]
