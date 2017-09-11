#coding=utf-8
from django.db import models

# 创建"个人信息"模型类,继承于Model
class UserInfo(models.Model):
    # 帐户
    Uname = models.CharField(max_length=20)
    # 密码
    Upwd = models.CharField(max_length=20)
    # 电话
    Utel =  models.CharField(max_length=20)
    # 邮箱
    Uemail = models.CharField(max_length=30)
    # 住址
    Uaddr = models.CharField(max_length=100)
    # 用户名是否有效(禁用)
    UisValid = models.BooleanField(default=True)
    # 帐号是否激活
    UisActive = models.BooleanField(default=False)

# 创建"收货地址"模型类,继承于Model
class ShippingAddr(models.Model):
    # 收货人姓名
    SAname = models.CharField(max_length=20)
    # 收货人电话
    SAtel = models.CharField(max_length=20)
    # 收货地址
    UshippingAddr = models.CharField(max_length=100)
    # 帐户连接到地址
    user = models.ForeignKey('UserInfo')
