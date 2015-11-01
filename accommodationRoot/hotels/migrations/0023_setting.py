# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0022_delete_setting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_format', models.CharField(default='european', max_length=12)),
                ('currency', models.CharField(default='\xa3', max_length=12)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
