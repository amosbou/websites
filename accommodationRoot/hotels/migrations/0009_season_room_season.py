# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0008_roomseason'),
    ]

    operations = [
        migrations.AddField(
            model_name='season',
            name='room_season',
            field=models.ManyToManyField(to='hotels.Room', through='hotels.RoomSeason'),
            preserve_default=True,
        ),
    ]
