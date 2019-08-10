from django.contrib import admin
from booktest.models import BookInfo,HeroInfo
#后台管理相关文件
#  Register your models here.

# 自定义显示的管理界面类容
class BookInfoAdmin(admin.ModelAdmin):
    '''图书模型管理类'''
    list_display = ['id','btitle','bpub_date']

class HeroInfoAdmin(admin.ModelAdmin):
    '''英雄人物模型管理类'''
    list_display = ['id','hname','hcomment','hbook']

# 注册模型类，第一个参数：在管理界面注册这个类，第二个参数：绑定在这个类上面
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)