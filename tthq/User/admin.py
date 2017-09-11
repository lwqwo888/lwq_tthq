from django.contrib import admin
from .models import *

# Register your models here.
# 装饰器管理类
@admin.register(UserInfo)
class UIadmin(admin.ModelAdmin):
    # 每页显示多少条数据
    list_per_page = 10
    #  “操作选项”的位置
    actions_on_top = True
    actions_on_bottom = True
    # 指定显示列表中的列,默认只显示第一列
    list_display = ['ADname','ADpwd','ADtel','ADemail','ADaddr','ADisValid','ADisActive',]
    # 更改列标题名


# admin.site.register(UserInfo)
admin.site.register(ShippingAddr)