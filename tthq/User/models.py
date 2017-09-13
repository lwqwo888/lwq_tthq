#coding=utf-8
from django.db import models

# 创建"个人信息"模型类,继承于Model
class UserInfo(models.Model):
    # 帐户
    Uname = models.CharField(verbose_name='用户名',max_length=20)
    # 密码  SHA512有512bits所以这里设置长度为600
    Upwd = models.CharField(verbose_name='密码',max_length=600)
    # 电话
    Utel =  models.CharField(verbose_name='用户电话',max_length=20)
    # 邮箱
    Uemail = models.CharField(verbose_name='用户邮箱',max_length=30)
    # 住址
    Uaddr = models.CharField(verbose_name='用户住址',max_length=100)
    # 用户名是否有效(禁用)
    UisValid = models.BooleanField(verbose_name='账户状态',default=True)
    # 帐号是否激活
    UisActive = models.BooleanField(verbose_name='账户是否激活',default=False)

    def __str__(self):
        return self.Uname

    # 定义一个方法来改变模型类对象的名称,用这个方法时不需要上面的str方法.使用这种方法可自定义显
    # 示列名.但是和verbose_name=相比的缺点也很大,不能在新增信息时显示自定义名
    # 称,只能显示添加后的.
    # def AD_Uname(self):
    #     return self.Uname
    # def AD_Upwd(self):
    #     return self.Upwd
    # def AD_Utel(self):
    #     return self.Utel
    # def AD_Uemail(self):
    #     return self.Uemail
    # def AD_Uaddr(self):
    #     return self.Uaddr
    # def AD_UisValid(self):
    #     return self.UisValid
    # def AD_UisActive(self):
    #     return self.UisActive
    # AD_Uname.short_description = "用户名"
    # AD_Upwd.short_description = '密码'
    # AD_Utel.short_description = '用户电话'
    # AD_Uemail.short_description = '用户邮箱'
    # AD_Uaddr.short_description = '用户住址'
    # AD_UisValid.short_description = '账号状态是否正常'
    # AD_UisActive.short_description = '是否激活'

# 创建"收货地址"模型类,继承于Model
class ShippingAddr(models.Model):
    # 收货人姓名
    SAname = models.CharField(verbose_name='收货人姓名',max_length=20)
    # 收货人电话
    SAtel = models.CharField(verbose_name='收货人电话',max_length=20)
    # 收货地址
    UshippingAddr = models.CharField(verbose_name='收货地址',max_length=100)
    # 帐户连接到地址
    user = models.ForeignKey('UserInfo')

    # def AD_SAname(self):
    #     return self.SAname
    # def AD_SAtel(self):
    #     return self.SAtel
    # def AD_UshippingAddr(self):
    #     return self.UshippingAddr
    # AD_SAname.short_description = '收货人姓名'
    # AD_SAtel.short_description = '收货人电话'
    # AD_UshippingAddr.short_description = '收货人地址'

    # 返回模型类的用户姓名,相当于返回ID,这里用于在admin里新增信息时显示可选择的
    # 外键,return将属性内容(如SAname的内容是收货人的姓名)直接返回到选择框,没有
    # 这个方法的话显示对象,则无法分辨选择的是什么.
    def __str__(self):
        return self.SAname
