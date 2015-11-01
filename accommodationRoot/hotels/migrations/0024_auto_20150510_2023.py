# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0023_setting'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setting',
            old_name='currency',
            new_name='currency_symbol',
        ),
    ]
