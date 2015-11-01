# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0013_auto_20150308_2005'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='roomseason',
            unique_together=set([('room', 'season')]),
        ),
    ]
