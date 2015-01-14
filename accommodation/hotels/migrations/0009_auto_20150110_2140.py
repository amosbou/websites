# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0008_auto_20150110_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_description_long',
            field=models.CharField(default=b'room long description', max_length=1000),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room',
            name='room_description_short',
            field=models.CharField(default=b'room short description', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='calendar',
            name='calendar_name',
            field=models.CharField(default=b'calendar name', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='room',
            name='room_caption',
            field=models.CharField(default=b'room caption', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(default=b'room type', max_length=200),
            preserve_default=True,
        ),
    ]
