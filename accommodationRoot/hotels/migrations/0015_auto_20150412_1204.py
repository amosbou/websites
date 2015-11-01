# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0014_auto_20150309_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='extra_rate_for_additional_guest',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room',
            name='extra_rate_percentage_for_additional_guest',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room',
            name='num_of_guests_for_base_rate',
            field=models.IntegerField(default=2),
            preserve_default=True,
        ),
    ]
