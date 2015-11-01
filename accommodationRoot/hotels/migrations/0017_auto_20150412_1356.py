# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0016_room_num_of_guests_increment_for_extra_rate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='extra_rate_for_additional_guest',
            new_name='extra_rate_for_guests_increment',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='extra_rate_percentage_for_additional_guest',
            new_name='extra_rate_percentage_for_guests_increment',
        ),
    ]
