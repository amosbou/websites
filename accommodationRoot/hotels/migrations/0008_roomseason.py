# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0007_auto_20150308_1824'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomSeason',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', models.FloatField(default=100)),
                ('room', models.ForeignKey(to='hotels.Room')),
                ('season', models.ForeignKey(to='hotels.Season')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
