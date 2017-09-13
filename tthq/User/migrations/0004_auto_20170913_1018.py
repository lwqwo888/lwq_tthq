# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_auto_20170913_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='Upwd',
            field=models.CharField(max_length=600, verbose_name='密码'),
        ),
    ]
