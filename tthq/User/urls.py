from django.conf.urls import url
from . import views
urlpatterns=[

    url(r'^register/$',views.register),
    url(r'^login/$',views.login),
    url(r'^info/$',views.user_input),# 录入用户注册信息
    # url(r'^log/$',views.log),
    url(r'^jason/$',views.detection_name),# 验证用户名是否存在
    url(r'^active(\d+)/$',views.active),
    url(r'^logging/$',views.logging),# 激活跳登录界面
    url(r'^font/$', views.font),#　炫酷字体
    url(r'^random/$', views.Verification_code),# 产生验证码
    url(r'^login_handle/$',views.login_handle),# 登录判断
    url(r'^$',views.index),

]

