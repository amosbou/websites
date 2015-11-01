# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0028_auto_20150713_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageLayer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=500)),
                ('order', models.IntegerField(default=1)),
                ('room_image', models.ForeignKey(to='hotels.RoomImage')),
            ],
        ),
    ]
