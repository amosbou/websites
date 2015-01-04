# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0002_auto_20141226_2105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('calendar_data', models.CharField(max_length=1000)),
                ('room', models.ForeignKey(to='hotels.Room')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
