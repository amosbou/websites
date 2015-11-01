# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0006_auto_20150307_2027'),
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
        migrations.DeleteModel(
            name='RoomSeason',
        ),
    ]
