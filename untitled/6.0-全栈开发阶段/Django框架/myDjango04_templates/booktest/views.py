from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from booktest.models import BookInfo

# Create your views here.
# /index

def login_required(view_func):
    '''登录判断装饰器'''
    def wrapper(request,*args,**kwargs):
        if  not request.session.has_key('islogin'):
            # 如果session中没有登录状态的标记，那么就返回到登录页
            return redirect('/login')
        else:
            # 如果session中存在登录状态的标记，那么就将视图函数对象
            return view_func(request,*args,**kwargs)
    return wrapper



# /index
def index(request):
    '''模板文件'''
    return render(request,'booktest/index.html')

# /temp_val
def temp_val(request):
    '''模板变量'''
    my_dict = {'title':'字典中的title'}
    my_list = [1,2,3]
    books = BookInfo.objects.get(id=1)
    context = {'my_dict':my_dict,'my_list':my_list,'books':books}
    return render(request,'booktest/temp_val.html',context)

# /temp_tags
def temp_tags(request):
    '''模板标签'''
    # 1.获取所有图书信息
    books = BookInfo.objects.all()

    return render(request,'booktest/temp_tags.html',{'books':books})

def temp_filter(request):
    '''模板过滤器'''
    # 1.获取所有图书信息
    books = BookInfo.objects.all()

    return render(request,'booktest/temp_filter.html',{'books':books})


#   /login
def login(request):
    '''显示登入页'''
    # 获取session来识别登入状态,
    if request.session.has_key('islogin'):
    # 若用户已经登入
        return redirect('/change_pwd')
    else:
    # 若用户未登入
        # 获取cookie username,所有的cookie信息存储在COOKIES字典中
        if 'username' in request.COOKIES:
            # 获取记住的用户名
            username = request.COOKIES['username']
        else:
            username = ''
        return render(request,'booktest/login.html',{'username':username})

#   /login_check
def login_check(request):
    '''对传过来的账号密码进行校验'''

    # 1.获取传过来的参数
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')

    # 获取输入的验证码和session中的验证码，并且转换成小写（不区分大小写）
    verifycode1 = request.POST.get('verifycode').lower()
    verifycode2 = request.session['verifycode'].lower()
    # print(remember)
    if not verifycode1 == verifycode2:
        '''判断验证码是否正确'''
        # 直接全部刷新页面
        # return redirect('/login')
        # ajax请求局部刷新
        return JsonResponse({'res':0})
    else:
        # 2.对传过来的参数进行校验
        if username=='smart' and password=='123':
            # 3.用户名密码正确，返回应答
            response =  JsonResponse({'res':2})  # 重定向
            if remember == 'on':
                # 设置cookie  username过期时间为7天
                response.set_cookie('username',username,max_age=7*24*3600)
            # 给session设置登入状态,只要有islogin就表示用户已经登入
            request.session['islogin']= True
            # 将账号存入session中
            request.session['username']= username
            return response
        else:
            return JsonResponse({'res':1})   #重定向


@login_required
# /change_pwd
def change_pwd(request):
    '''显示修改密码界面'''
    # 有些页面只能用户登入后才能访问，这样需要加入判断
    # if not request.session.has_key('islogin'):
    #     return redirect('/login')

    return render(request,'booktest/change_pwd.html')

@login_required
# /change_pwd_action
def change_pwd_action(request):
    '''显示密码修改成功页面'''

    # if not request.session.has_key('islogin'):
    #     return redirect('/login')

    # 1.获取账号和新密码
    password = request.POST.get('password')
    username = request.session.get('username')
    # 2.将新密码存入数据库，修改对应账号的密码
    # 3.修改后的密码传入到前台
    return HttpResponse('%s修改后的密码为:%s'%(username,password))

# /url_reverse
def url_reverse(request):
    '''url反向解析页面'''
    return render(request,'booktest/url_reverse.html')

# /show_args
def show_args(request,a,b):
    '''位置参数url反向解析'''
    return HttpResponse(a+':'+b)

def show_kwargs(request,c,d):
    '''关键字参数url反向解析'''
    return HttpResponse(c+':'+d)

from django.core.urlresolvers import reverse

def a_url_reverse(request):
    # 视图中重定向无参数使用
    # url = reverse('booktest:index')
    # 视图中重定向 位置参数的url反向解析使用
    # url = reverse('booktest:show_args',args=(1,2))
    # 视图中重定向关键字参数的url反向解析使用
    url = reverse('booktest:show_kwargs',kwargs={'c':3,'d':4})
    return redirect(url)





from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO
def verify_code(request):
    # 显示验证码
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0qwertyuioplkjhgfdsazxcvbnm'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('/static/font/FreeMono.ttf', 23)
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    #内存文件操作
    buf = BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')












