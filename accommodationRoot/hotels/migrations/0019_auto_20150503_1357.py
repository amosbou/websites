# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0018_room_unique_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='unique_id',
            new_name='code',
        ),
    ]
