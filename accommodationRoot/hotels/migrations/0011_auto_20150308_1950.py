# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0010_auto_20150308_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomSeason',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', models.FloatField(default=100)),
                ('room', models.ForeignKey(to='hotels.Room')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('room_season', models.ManyToManyField(to='hotels.Room', through='hotels.RoomSeason')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='roomseason',
            name='season',
            field=models.ForeignKey(to='hotels.Season'),
            preserve_default=True,
        ),
    ]
