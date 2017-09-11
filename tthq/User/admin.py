from django.contrib import admin
from .models import *

# Register your models here.
# 装饰器管理类(用户信息)
@admin.register(UserInfo)
class UIadmin(admin.ModelAdmin):
    # 每页显示多少条数据
    list_per_page = 10
    #  “操作选项”的位置
    actions_on_top = True
    actions_on_bottom = True
    # 指定显示列表中的列,默认只显示第一列
    list_display = ['Uname','Upwd','Utel','Uemail','Uaddr','UisValid','UisActive']
    # 指定显示列表中的列,默认只显示第一列,这里中括号里的名称是models里自定义的改名方法的方法名.
    # list_display = ['AD_Uname','AD_Upwd','AD_Utel','AD_Uemail','AD_Uaddr','AD_UisValid','AD_UisActive',]

# 管理器有两种使用方式,一中是上面的装饰器,另外是下面被注释掉的"注册",这里我们使用功能更多的装饰器
# admin.site.register(UserInfo)
# admin.site.register(ShippingAddr)

# 装饰器管理器(收货地址)
@admin.register(ShippingAddr)
class SPadmin(admin.ModelAdmin):
    list_per_page = 10
    actions_on_top = True
    actions_on_bottom = True
    list_display = ['SAname','SAtel','UshippingAddr']