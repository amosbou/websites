# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0004_auto_20150102_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendar',
            name='calendar_name',
            field=models.CharField(default='unknown', max_length=200),
            preserve_default=False,
        ),
    ]
