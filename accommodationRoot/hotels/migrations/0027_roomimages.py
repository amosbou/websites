# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0026_auto_20150604_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(max_length=500)),
                ('purpose', models.CharField(max_length=50)),
                ('resolution', models.CharField(max_length=100)),
                ('order', models.IntegerField(default=1)),
                ('room', models.ForeignKey(to='hotels.Room')),
            ],
        ),
    ]
