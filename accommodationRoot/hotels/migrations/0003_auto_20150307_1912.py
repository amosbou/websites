# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0002_auto_20150307_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='addresses',
        ),
        migrations.AddField(
            model_name='address',
            name='guest',
            field=models.ForeignKey(default=1, to='hotels.Guest'),
            preserve_default=False,
        ),
    ]
