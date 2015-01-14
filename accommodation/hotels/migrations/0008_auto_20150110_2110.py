# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0007_auto_20150110_2001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='room_num_of_beds',
            new_name='room_max_num_of_guests',
        ),
        migrations.AddField(
            model_name='room',
            name='room_double_bed_num_of',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room',
            name='room_double_bed_size',
            field=models.CharField(default=b'Double', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room',
            name='room_single_bed_num_of',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room',
            name='room_single_bed_size',
            field=models.CharField(default=b'Single', max_length=200),
            preserve_default=True,
        ),
    ]
