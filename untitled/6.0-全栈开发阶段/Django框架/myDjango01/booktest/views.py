from django.shortcuts  import  render
from django.http import HttpResponse
from booktest.models import BookInfo ,HeroInfo#导入图书模型类
from django.template import  loader,RequestContext

# def my_render(requst,template_path,context_dict={''}):
#     # 1.加载模板文件，模板对象
#     temp = loader.get_template(template_path)
#     # 2.定义模板上下文: 给模板文件传递数据
#     context = RequestContext(requst,context_dict)
#     # 3.模板渲染: 产生标准的html类容
#     res_html = temp.render(context)
#     # 4.返回给浏览器
#     return HttpResponse(res_html)

# Create your views here.
# 1.定义视图函数，HttpResponse
# 2.进行url的匹配，建立url地址与视图的关联

def index(request):
    # 进行处理，M 和 T进行交互....
    # return HttpResponse('老铁，没毛病')
    # 自己定义的方法函数
    # return my_render(request,'booktest/index.html')
    # Django封装的方法
    return render(request,'booktest/index.html',{'content':'hello python','list':list(range(1,10))})


def index2(request):

    return  HttpResponse('hello python')

# /books
def show_books(request):
    '''显示图书的信息'''
    # 1.通过M查找图书信息
    books = BookInfo.objects.all()
    # 2.使用模板
    return render(request,'booktest/show_books.html',{'books':books})

# /book/(\d+)
def detail(request,pid):
    '''显示英雄信息'''
    # 1.根据bid查询图书信息
    book = BookInfo.objects.get(id=pid)
    # 2.查询图书关联的英雄信息
    # heros = book.heroinfo_set.all()
        # 关联查询，通过模型类查询：
    heros = HeroInfo.objects.filter(hbook__id=pid)
    # 3.使用模板
    return render(request,'booktest/detail.html',{'book':book,'heros':heros})











