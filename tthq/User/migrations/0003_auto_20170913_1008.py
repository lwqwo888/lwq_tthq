# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20170911_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddr',
            name='SAname',
            field=models.CharField(max_length=20, verbose_name='收货人姓名'),
        ),
        migrations.AlterField(
            model_name='shippingaddr',
            name='SAtel',
            field=models.CharField(max_length=20, verbose_name='收货人电话'),
        ),
        migrations.AlterField(
            model_name='shippingaddr',
            name='UshippingAddr',
            field=models.CharField(max_length=100, verbose_name='收货地址'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='Uaddr',
            field=models.CharField(max_length=100, verbose_name='用户住址'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='Uemail',
            field=models.CharField(max_length=30, verbose_name='用户邮箱'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='UisActive',
            field=models.BooleanField(default=False, verbose_name='账户是否激活'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='UisValid',
            field=models.BooleanField(default=True, verbose_name='账户状态'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='Uname',
            field=models.CharField(max_length=20, verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='Upwd',
            field=models.CharField(max_length=70, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='Utel',
            field=models.CharField(max_length=20, verbose_name='用户电话'),
        ),
    ]
