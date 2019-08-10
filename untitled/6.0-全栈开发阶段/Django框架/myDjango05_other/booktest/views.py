from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.conf import settings
from booktest.models import PicTest,AreaInfo
# Create your views here.


EXCLUDE_IPS = ['127.0.0.1']
def blocked_ips(view_func):
    '''禁止某些ip访问'''
    def wrapper(request,*args,**kwargs):
        # 获取浏览器ip地址
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in EXCLUDE_IPS:
            return HttpResponse('<h1>禁止访问</h1>')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper

# @blocked_ips
# /static_test
def static_test(request):
    '''显示图片'''
    return render(request,'booktest/static_test.html')

# @blocked_ips
def index(request):
    '''首页'''
    print('========index')
    return render(request,'booktest/index.html')




def show_load(request):
    '''显示上传文件页面'''
    return render(request,'booktest/upload_pic.html')

def upload_handle(request):
    '''上传图片处理'''
    # 1.获取上传文件的处理对象
    pic = request.FILES['pic']
    # print(type(pic))
    # print(pic)
    # print(type(pic.name))
    from django.conf import settings
    # 2.创建一个文件
    save_path = '%s/booktest/%s'%(settings.MEDIA_ROOT,pic.name)
    #创建文件
    with open(save_path,'wb') as f:
        # 3.获取上传文件的类容并写入到创建的文件中
        for content in pic.chunks():
            f.write(content)

    # 4.在数据库中保存上传记录
    PicTest.objects.create(goods_pic = 'booktest/%s'%pic.name)

    return HttpResponse('ok')

from django.core.paginator import Paginator
# /show_area(\d*)
def show_area(request,pindex):
    '''显示省市级页面'''
    # 1.查询所有省级信息
    areas = AreaInfo.objects.filter(aParent__isnull=True)
    # 2.分页，按照每页10条数据
    paginator = Paginator(areas,10)
        #判断传过来的字符串
    if pindex == '':
        pindex = 1
    else:
        pindex = int(pindex)
    # 3.获取当前页对象
    page = paginator.page(pindex)
    # 2.返回
    return render(request,'booktest/show_area.html',{'page':page})

# /areas
def areas(request):
    '''显示省市县下拉框'''
    return render(request,'booktest/areas.html')

# /prov
def prov(request):
    '''获取所有省级地区信息'''
    # 1.获取所有的省级地区信息
    areas = AreaInfo.objects.filter(aParent__isnull=True)
    # 2.拼接成json数据
    areas_list =[]
    for area in areas:
        areas_list.append((area.id,area.atitle))

    return JsonResponse({'data':areas_list})

# /city
def city(request,pid):
    '''获取相应省的市级地区'''
    # 1.获取相应省的市级地区
    # areas = AreaInfo.objects.get(id=pid).areainfo_set.all()
    areas = AreaInfo.objects.filter(aParent__id=pid)
    # 2.拼接成json数据
    areas_list = []
    for area in areas:
        areas_list.append((area.id, area.atitle))

    return JsonResponse({'data':areas_list})
# /dis
def dis(request,pid):
    '''获取市级相应的县'''
    # 1.获取相应市的县级地区
    # areas = AreaInfo.objects.get(id=pid).areainfo_set.all()
    areas = AreaInfo.objects.filter(aParent__id=pid)
    # 2.拼接成json数据
    areas_list = []
    for area in areas:
        areas_list.append((area.id, area.atitle))

    return JsonResponse({'data': areas_list})


