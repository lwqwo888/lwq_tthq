from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *
from hashlib import sha512
from django.conf import settings
from django.core.mail import send_mail
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
    # 构建邮件内容
    msg = "<div>Email 地址验证<br><br>" \
          "尊敬的: <span style='font-size: 28px;'><B>%s</B></span><br>" \
          "这封信是由 <B>天天花钱网</B> 发送的。<br><br>" \
          "您收到这封邮件，是由于在 <B>天天花钱网</B> 进行了新用户注册，或用户修改 Email 使用 了这个邮箱地址。如果您并没有访问过 <B>天天花钱网</B>，或没有进行上述操作，请忽 略这封邮件。您不需要退订或进行其他进一步的操作。<br><br>" \
          "----------------------------------------------------------------------<br>" \
          "帐号激活说明<br>" \
          "----------------------------------------------------------------------<br><br>" \
          "如果您是 <B>天天花钱网</B> 的新用户，或在修改您的注册 Email 时使用了本地址，我们需要对您的地址有效性进行验证以避免垃圾邮件或地址被滥用。<br>" \
          '您只需点击下面的"立即激活"即可激活您的帐号：<br>' \
          "<a href='http://127.0.0.1:8000/User/active%d/'>-------->立即激活<--------</a><br>" \
          '(如果上述方法未能激活,请"<a href="http://127.0.0.1:8000/index/">点此进入</a>"<B>天天花钱网</B>首页,点击下方联系我们,客服妹妹将为您激活)<br><br>' \
          "<B>感谢您的访问，祝您使用愉快！</B><br><br>" \
          "<B>此致</B>!<br>"\
          "<B>天天花钱网 扶她 管理团队.</B><br>" \
          "</div>"%(user.Uname,user.id)
    # 邮件主题,邮件来源,收件人,邮件内容
    send_mail('天天花钱用户激活','',settings.EMAIL_FROM,[uemail],html_message=msg)
    return HttpResponse('邮件已发送,请到邮箱激活')

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

    dname = UserInfo.objects.filter(Uname__contains=lname)

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
    return HttpResponse("账户以激活,<a href='/User/login/'>点击登录</a>")