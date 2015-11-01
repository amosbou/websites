# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0015_auto_20150412_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='num_of_guests_increment_for_extra_rate',
            field=models.IntegerField(default=2),
            preserve_default=True,
        ),
    ]
