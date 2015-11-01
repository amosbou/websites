# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guest',
            old_name='address',
            new_name='addresses',
        ),
    ]
