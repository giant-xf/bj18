from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

# Create your views here.

def index(request):
    '''显示首页'''
    return render(request,'booktest/index.html')

def show_arg(request,num):
    '''返回参数'''
    return HttpResponse(num)

def login(request):
    '''显示登入页'''
    # 获取session来识别登入状态,
    if request.session.has_key('islogin'):
    # 若用户已经登入
        return redirect('/index')
    else:
    # 若用户未登入
        # 获取cookie username
        if 'username' in request.COOKIES:
            # 获取记住的用户名
            username = request.COOKIES['username']
        else:
            username = ''
        return render(request,'booktest/login.html',{'username':username})

def login_check(request):
    '''对传过来的账号密码进行校验'''
    # request.POST
    # 保存的是post提交的参数 QueryDict类型
    # QueryDict可以保存相同键的不同的值，默认get()返回最后一个，调用getlist('a')可以返回所有值的列表类型
    print(request.method)
    print(request.path)
    # request.GET 保存的是get提交参数
    # 1.获取传过来的参数
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    # print(remember)

    # 2.对传过来的参数进行校验
    if username=='smart' and password=='123':
        # 3.用户名密码正确，返回应答
        response =  redirect('/index')  # 重定向
        if remember == 'on':
            # 设置cookie  username过期时间为7天
            response.set_cookie('username',username,max_age=7*24*3600)
        # 给session设置登入状态,只要有islogin就表示用户已经登入
        request.session['islogin']= True
        return response
    else:
        return redirect('/login')   #重定向

def login_ajax(request):
    '''显示ajax登入页面'''
    return render(request,'booktest/login_ajax.html')

def login_ajax_check(request):
    '''ajax账号密码校验'''
    # 1.获取账号和密码
    username = request.POST.get('username')
    password = request.POST.get('password')


    # 2.校验账号和密码，返回应答
    if username=='smart' and password=='123':
        # 用户名密码正确
        return JsonResponse({'res':1})
    else:
        # 用户名密码错误
        return JsonResponse({'res':0})

# /set_cookie
def set_cookie(request):
    '''设置cookie'''
    response = HttpResponse('设置cookie')
    # 设置一个cookie信息，名字为num，值为1
    response.set_cookie('num',1,max_age=3600)
    # 返回reponse
    return response

# /get_cookie
def get_cookie(request):
    '''获取cookie'''
    # 取出cookie中num的值,cookie都以字典的形式存储在COOKIES中
    num = request.COOKIES['num']
    return HttpResponse(num)

# / set_session
def set_session(request):
    '''设置session信息'''
    # 里面的信息base64编码
    request.session['name']='smart'
    request.session['age'] =18
    return HttpResponse("设置成功")

# / get_session
def get_session(request):
    '''获取session信息'''
    name = request.session['name']
    age = request.session['age']
    return HttpResponse(name+' : '+str(age))

# / clear_session
def clear_session(request):
    '''删除session信息'''
    # del request.session['name']   # 删除某一个键值
    #request.session.clear() # 删除数据部分
    request.session.flush()     # 删除全部信息
    return HttpResponse('删除成功')




def show_reqarg(request):
    '''接收请求参数'''
    if request.method == 'GET':
        a = request.GET.get('a') #获取请求参数a
        b = request.GET.get('b') #获取请求参数b
        c = request.GET.get('c') #获取请求参数c
        return render(request, 'booktest/show_reqarg.html', {'a':a, 'b':b, 'c':c})
    else:
        name = request.POST.get('uname') #获取name
        gender = request.POST.get('gender') #获取gender
        hobbys = request.POST.getlist('hobby') #获取hobby
        return render(request, 'booktest/show_postarg.html', {'name':name, 'gender':gender, 'hobbys':hobbys})




