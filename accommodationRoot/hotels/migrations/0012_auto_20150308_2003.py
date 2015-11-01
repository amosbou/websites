# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0011_auto_20150308_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='country',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='guest',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='room',
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.RemoveField(
            model_name='guestaddress',
            name='address',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.RemoveField(
            model_name='guestaddress',
            name='address_type',
        ),
        migrations.DeleteModel(
            name='AddressType',
        ),
        migrations.RemoveField(
            model_name='guestaddress',
            name='guest',
        ),
        migrations.DeleteModel(
            name='Guest',
        ),
        migrations.DeleteModel(
            name='GuestAddress',
        ),
        migrations.RemoveField(
            model_name='room',
            name='hotel',
        ),
        migrations.DeleteModel(
            name='Hotel',
        ),
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
            name='Room',
        ),
        migrations.DeleteModel(
            name='Season',
        ),
        migrations.DeleteModel(
            name='Settings',
        ),
    ]
