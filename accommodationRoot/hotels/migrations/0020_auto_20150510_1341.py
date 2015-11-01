# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0019_auto_20150503_1357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_format', models.CharField(default=b'european', max_length=12)),
                ('currency', models.CharField(default='\xa3', max_length=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Settings',
        ),
    ]
