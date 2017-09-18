from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *
from hashlib import sha512
from django.conf import settings
from django.core.mail import send_mail
import time

def index(requset):
    return render(requset,'Goods/index.html')
# 注册页面
def register(request):
    return render(request,'User/register.html')
# 登录页面
def login(request):
    return render(request,'User/login.html')
# 用户注册信息填写以及判断
def user_input(requset):
    # 创建一个requset.POST对象uif,获取用户输入的信息
    uif = requset.POST
    # 定义一个全局变量,为了下面注册时的是否有重复用户名使用
    uname = uif.get('user_name')
    upwd1 = uif.get('pwd')
    upwd2 = uif.get('cpwd')
    uemail = uif.get('email')
    context = {'user_name':uname,'pwd':upwd1,'cpwd':upwd2,'email':uemail}
    # 判断两次密码是否一致,如果一致继续向下执行,否则返回注册页面再注册一次.
    if upwd1 != upwd2:
        return render(requset,'/register.html',context)
    # 密码加密
    s1 = sha512()
    # 需要把密码转换成与数据库编码格式一样才能进行存储
    s1.update(upwd2.encode("utf8"))
    upwd3 = s1.hexdigest()
    # 存入数据库
    user = UserInfo()
    user.Uname=uname
    user.Upwd=upwd3
    user.Uemail=uemail
    user.save()
    # 发送激活邮件
    # 获取日期
    ymd = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    # 获取时间
    ms = time.strftime('%H:%M:%S', time.localtime(time.time()))
    # 构建邮件内容
    msg = '''    <div style="margin:0 auto; width:700px; box-shadow:0 0 10px rgba(0, 0, 0, 0.2); font-family:'Helvetica Neue',Helvetica,Arial,Microsoft YaHei,sans-serif;">
    ''' \
          '''        <div style="padding-left:180px; height:60px; line-height:63px; border-radius:3px 3px 0 0; font-size:18px; font-weight:100; color:#fff; background:url(http://upload.ouliu.net/i/20170914231020j8rl8.png) #337ab7 no-repeat 15px; overflow:hidden;"><span style="margin-left: 100px;">&#9;请激活您的帐号</span></div>
''' \
          '''        <div style="padding:15px 30px 93px; min-height:350px; font-size:14px; word-wrap:break-word; border:#c5c5c5 solid; border-width:0 1px; line-height:24px; overflow:hidden; position:relative;">
''' \
          '''            <p><strong style="font-size: 24px;">Hi，%s：</strong></p>
''' \
          '''            <p style="padding:5px 0; text-indent:2em;">您收到这封邮件，是由于在 天天花钱网 进行了新用户注册而使用了这个邮箱地址。如果您并没有访问过 天天花钱网，或没有进行上述操作，请忽略这封邮件，您不需要退订或进行其他任何操作，很抱歉打扰您。</p>
''' \
          '''            <b style="display:block; margin-top:30px; color:#c00;">帐号激活说明</b>
''' \
          '''            <p style="padding:5px 0; text-indent:2em;">如果您是 天天花钱网 的新用户，或在修改您的注册 Email 时使用了本地址，我们需要对您的地址有效性进行验证以避免垃圾邮件或地址被滥用。</p>
''' \
          '''            <p>您只需点击下面的链接，即可激活您的帐号，<span style="color:#c00;">为了保障帐号的安全性，请在2小时完成验证</span>：</p>
 ''' \
          '''            <div style="margin:10px 0; padding:10px; border:1px #67c4f0 solid; text-align:left; font-size:14px; background:#d9edf7;"><a href='http://127.0.0.1:8000/User/active%d/'>http://127.0.0.1:8000/User/active%d</a></div>
 ''' \
          '''            <p style="color:#666;">(如果上面不是链接形式，请将该地址手工粘贴到浏览器地址栏再访问)</p>
 ''' \
          '''            <p>感谢您的访问，祝您使用愉快！</p><div style="left:0; bottom:0; right:0; padding:15px; height:48px; background:#f0f0f0; text-align:right; position:absolute;"><a style="color:#05a; text-decoration:none; font-weight:700;" href="http://www.qdfuns.com/" target="_blank"> 天天花钱网 </a>管理组敬上<br><span style="border-bottom:1px dashed #ccc;" t="5" times=" %s">%s</span> %s</div>
 ''' \
          '''        </div>
 ''' \
          '''         <div style="height:10px; border-radius:0 0 3px 3px; border: 1px solid #c5c5c5; border-top: none; background:#337ab7 url(http://www.qdfuns.com/res/images/logos/mail/mailbottom.gif) repeat-x;"></div>
''' \
          '''    </div>''' %(user.Uname, user.id, user.id, ms,ymd,ms)

    # 邮件主题,邮件来源,收件人,邮件内容
    send_mail('天天花钱用户激活','',settings.EMAIL_FROM,[uemail],html_message=msg)
    context = {'email':uemail}
    print(context)
    return render(requset, 'User/font-demo.html', context)

    # 用redirect重新去请求匹配login正则,就可以跳转到登录页面了,或者使用render方式返回login.html
    # return redirect('/login/')
    # return render(requset, 'User/login.html')

# 用户登录信息填写以及判断
def log(requset):
    # 创建一个request.POST对象ulog
    ulog = requset.POST

    # dname---< class 'str'> 获取用户输入的用户名是字符串类型.
    lname = ulog.get('username')

    lpwd = ulog.get('pwd')

    dname = UserInfo.objects.filter(Uname=lname)

    # <class 'User.models.UserInfo'> 获取数据库里保存的用户名是对象.
    dname1 = str(dname[0])
    # 分别打印dname1和lname可以看到是不同类型的相同值,
    # 所以要把dname转字符串才能比较
    print(type(dname1),type(lname))


    # return render(requset,'/User/index.html',dname1)
    # 如果用户输入的账号存在于数据库则通过
    if lname == dname1:
        return render(requset,'Goods/index.html')
    # else:
        # return render(requset,)
# 检查用户名可用性
def detection_name(requset):
    # 方法一
    # 获取ajax传来的字典,键为'jason',通过键获取值(用户输入的用户名)
    uname = requset.GET.get('jason')
    # 查询输入的用户名是否存在于数据库,如果存在那么count计数不可能为0,非0就说明已存在
    count = UserInfo.objects.filter(Uname=uname).count()
    print(count)

    # count是字典类型,所以返回键值对
    return JsonResponse({'count':count})

    # # 方法二
    # # get方法获取ajax数据
    # dict = requset.GET
    # uname = dict.get('jason')
    # dname = UserInfo.objects.filter(Uname=uname)
    # # 如果dname的值是空,为了防止空值下标越界,直接return False
    # if len(dname) == 0:
    #     return HttpResponse('False')
    #
    #     # print('kongkongkong')
    # else: # 否则就取出下标对应的值进行对比.
    #     dname1 = str(dname[0])
    # # dname是数据库里的用户名,如果和用户输入的相同,则返回True给前台做判断
    #     if uname == dname1:
    #         return HttpResponse("True")
    #     else:
    #         return HttpResponse('False')

# 发送激活邮件
def active(request,uid):
    # 获取用户对象
    user = UserInfo.objects.get(id=uid)
    # 激活用户
    user.UisActive = True
    # 保存
    user.save()
    # context = {}
    return render(request,'User/logging.html')
def font(requset):
    return render(requset, 'User/temp/../templates/User/font-demo.html')

def logging(requset):# 临时,可删
    return render(requset,'User/logging.html')