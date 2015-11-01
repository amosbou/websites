# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0027_roomimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(max_length=500)),
                ('purpose', models.CharField(max_length=50)),
                ('resolution', models.CharField(max_length=100)),
                ('order', models.IntegerField(default=1)),
                ('room', models.ForeignKey(to='hotels.Room')),
            ],
        ),
        migrations.RemoveField(
            model_name='roomimages',
            name='room',
        ),
        migrations.DeleteModel(
            name='RoomImages',
        ),
    ]
