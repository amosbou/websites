# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0029_imagelayer'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagelayer',
            name='div_attributes',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
