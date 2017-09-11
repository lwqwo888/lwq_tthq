# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingAddr',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('SAname', models.CharField(max_length=20)),
                ('SAtel', models.CharField(max_length=20)),
                ('UshippingAddr', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Uname', models.CharField(max_length=20)),
                ('UpassWord', models.CharField(max_length=20)),
                ('Utel', models.CharField(max_length=20)),
                ('Uemail', models.CharField(max_length=30)),
                ('Uaddr', models.CharField(max_length=100)),
                ('UisValid', models.BooleanField(default=True)),
                ('UisActive', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='shippingaddr',
            name='user',
            field=models.ForeignKey(to='User.UserInfo'),
        ),
    ]
