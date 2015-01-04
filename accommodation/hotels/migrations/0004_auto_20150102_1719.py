# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0003_calendar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendar',
            name='id',
        ),
        migrations.AlterField(
            model_name='calendar',
            name='room',
            field=models.OneToOneField(primary_key=True, serialize=False, to='hotels.Room'),
            preserve_default=True,
        ),
    ]
