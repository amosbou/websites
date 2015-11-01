# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=254)),
                ('city', models.CharField(max_length=254)),
                ('zipcode', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('check_in_date', models.DateField(verbose_name=b'Check In')),
                ('check_out_date', models.DateField(verbose_name=b'Check Out')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name=b'Booking Date')),
                ('time_created', models.DateField(auto_now_add=True, verbose_name=b'Booking Time')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('iso_code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=254)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
                ('email_address', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=50)),
                ('address', models.ManyToManyField(to='hotels.Address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description_short', models.CharField(default=b'room short description', max_length=200)),
                ('description_long', models.CharField(default=b'room long description', max_length=1000)),
                ('caption', models.CharField(default=b'room caption', max_length=200)),
                ('type', models.CharField(default=b'room type', max_length=200)),
                ('double_bed_size', models.CharField(default=b'Double', max_length=200)),
                ('double_bed_num_of', models.IntegerField(default=1)),
                ('single_bed_size', models.CharField(default=b'Single', max_length=200)),
                ('single_bed_num_of', models.IntegerField(default=1)),
                ('max_num_of_guests', models.IntegerField(default=2)),
                ('rate', models.FloatField(default=100)),
                ('hotel', models.ForeignKey(to='hotels.Hotel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_format', models.CharField(default=b'dd/mm/yy', max_length=12)),
                ('currency', models.CharField(default='\xa3', max_length=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='booking',
            name='guest',
            field=models.ForeignKey(to='hotels.Guest'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(to='hotels.Room'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.ForeignKey(to='hotels.Country'),
            preserve_default=True,
        ),
    ]
