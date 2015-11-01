# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0004_remove_address_guest'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GuestAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.ForeignKey(to='hotels.Address')),
                ('address_type', models.ForeignKey(to='hotels.AddressType')),
                ('guest', models.ForeignKey(to='hotels.Guest')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
