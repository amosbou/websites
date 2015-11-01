# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0020_auto_20150510_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='currency',
            field=models.CharField(default='\xa3', max_length=12),
            preserve_default=True,
        ),
    ]
