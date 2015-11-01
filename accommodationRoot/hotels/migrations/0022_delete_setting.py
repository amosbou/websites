# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0021_auto_20150510_1839'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Setting',
        ),
    ]
