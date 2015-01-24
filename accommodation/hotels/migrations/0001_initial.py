# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('calendar_year', models.CharField(default=b'2999', max_length=10)),
                ('calendar_name', models.CharField(default=b'calendar name', max_length=200)),
                ('calendar_data', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hotel_name', models.CharField(max_length=200)),
                ('hotel_city', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room_name', models.CharField(max_length=200)),
                ('room_description_short', models.CharField(default=b'room short description', max_length=200)),
                ('room_description_long', models.CharField(default=b'room long description', max_length=1000)),
                ('room_caption', models.CharField(default=b'room caption', max_length=200)),
                ('room_type', models.CharField(default=b'room type', max_length=200)),
                ('room_double_bed_size', models.CharField(default=b'Double', max_length=200)),
                ('room_double_bed_num_of', models.IntegerField(default=1)),
                ('room_single_bed_size', models.CharField(default=b'Single', max_length=200)),
                ('room_single_bed_num_of', models.IntegerField(default=1)),
                ('room_max_num_of_guests', models.IntegerField(default=2)),
                ('room_rate', models.FloatField(default=100)),
                ('hotel', models.ForeignKey(to='hotels.Hotel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='calendar',
            name='room',
            field=models.ForeignKey(to='hotels.Room'),
            preserve_default=True,
        ),
    ]
