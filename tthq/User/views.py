from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

def register(request):
    return render(request,'User/register.html')
def login(request):
    return render(request,'User/login.html')
def info(requset):
    # 创建一个requset.POST对象uif
    uif = requset.POST
    uname = uif.get('user_name')
    upwd1 = uif.get('pwd')
    upwd2 = uif.get('cpwd')
    uemail = uif.get('email')
    context = {'user_name':uname,'pwd':upwd1,'cpwd':upwd2,'email':uemail}
    # 判断两次密码是否一致,如果一致继续向下执行,否则返回注册页面再注册一次.
    if upwd1 != upwd2:
        return render(requset,'/register.html',context)

    user = UserInfo()
    user.Uname=uname
    user.Upwd=upwd2
    user.Uemail=uemail
    user.save()
    # 用redirect重新去请求匹配login正则,就可以跳转到登录页面了,或者使用render方式返回login.html
    # return redirect('/login/')
    return render(requset, 'User/login.html')
def log(requset):
    # 创建一个request.POST对象ulog
    ulog = requset.POST
    lname = ulog.get('name_input')
    lpwd = ulog.get('pass_input')
    