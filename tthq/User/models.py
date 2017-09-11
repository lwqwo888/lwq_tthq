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

    # def __str__(self):
        # return self.Uname
    # 定义一个方法来改变模型类对象的名称
    def ADname(self):
        return self.Uname
    def ADpwd(self):
        return self.Upwd
    def ADtel(self):
        return self.Utel
    def ADemail(self):
        return self.Uemail
    def ADaddr(self):
        return self.Uaddr
    def ADisValid(self):
        return self.UisValid
    def ADisActive(self):
        return self.UisActive
    ADname.short_description = "用户名"
    ADpwd.short_description = '密码'
    ADtel.short_description = '用户电话'
    ADemail.short_description = '用户邮箱'
    ADaddr.short_description = '用户住址'
    ADisValid.short_description = '账号状态是否正常'
    ADisActive.short_description = '是否激活'

# 创建"收货地址"模型类,继承于Model
class ShippingAddr(models.Model):
    # 收货人姓名
    SAname = models.CharField(verbose_name='收货人姓名',max_length=20)
    # 收货人电话
    SAtel = models.CharField(verbose_name='收货人电话',max_length=20)
    # 收货地址
    UshippingAddr = models.CharField(max_length=100)
    # 帐户连接到地址
    user = models.ForeignKey('UserInfo')
    def __str__(self):
        return self.SAname
