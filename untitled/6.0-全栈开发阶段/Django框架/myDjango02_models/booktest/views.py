from django.shortcuts import render,redirect #导入重定向函数
from booktest.models import BookInfo,AreaInfo
from datetime import date
from django.http import HttpResponse,HttpResponseRedirect #重定向
from django.db.models import F,Q
# Create your views here.

def index(request):
    '''显示图书信息'''
    # 1.查询出所有图书信息
    books = BookInfo.objects.all()
    # 2.使用模板
    return render(request,'booktest/index.html',{'books':books})

def create(request):
    '''新增图书'''
    # 1.创建图书对象
    book = BookInfo()
    # 2.给新增图书添加属性
    book.btitle = '流星蝴蝶剑'
    book.bpub_date = date(1992,1,3)
    # 3.保存进数据库
    book.save()
    # 4.重定向访问/index
    # return HttpResponseRedirect('/index') #将页面重定向到index页面
    return redirect('/index')

def delete(request,bid):
    '''删除图书'''
    # 1.获取要删除的图书对象
    book = BookInfo.objects.get(id = bid)
    # 2.删除对象
    book.delete()
    # 3.重定向访问/index
    # return HttpResponseRedirect('/index')
    return redirect('/index')

def areas(request):
    '''显示广州市的上级省和下级区'''
    # 1.获取当前市
    area = AreaInfo.objects.get(atitle='广州市')
    # 2.获取当前市的父级
    parent = area.aParent
    # 3.获取下级区
    childen = area.areainfo_set.all()
    return render(request,'booktest/areas.html',{'area':area,'parent':parent,'childen':childen})



