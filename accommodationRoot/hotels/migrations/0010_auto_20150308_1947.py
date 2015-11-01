# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0009_season_room_season'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomseason',
            name='room',
        ),
        migrations.RemoveField(
            model_name='roomseason',
            name='season',
        ),
        migrations.RemoveField(
            model_name='season',
            name='room_season',
        ),
        migrations.DeleteModel(
            name='RoomSeason',
        ),
        migrations.DeleteModel(
            name='Season',
        ),
    ]
