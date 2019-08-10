from django.db import models

# Create your models here.

class BookInfoManage(models.Manager):
    '''图书模型管理器类'''

    # 1.改变查询结果集
    def all(self):
        # 1.调用父类的all，获取所有数据
        books = super().all()
        # 2.对数据进行过滤
        book = books.filter(isDelete=False)
        #返回结果集
        return  book
    # 2.封装函数：操作模型类对应的数据表(增删改查)
    def create_book(self,btitle,bpub_date):
        # 1.创建一个图书对象
            #获取self所在的模型类
        model_class = self.model
        book = model_class()
        # book = BookInfo()     #固定获取，无法应对类名的更改
        book.btitle = btitle
        book.bpub_date = bpub_date
        # 2.保存进数据库
        book.save()
        # 3.返回book
        return book



class BookInfo(models.Model):
    '''图书信息类'''
    # 图书名
    btitle = models.CharField(max_length=20)
    # 图书出版日期
    bpub_date = models.DateField()
    # 阅读量
    bread = models.IntegerField(default=0)
    # 评论量
    bcomment = models.IntegerField(default=0)
    # 删除标记
    isDelete = models.BooleanField(default=False)

    objects = BookInfoManage()

    class Mate:
        db_table = 'booktest_bookinfo' #元选项，指定模型类的表名，


class HeroInfo(models.Model):
    '''英雄人物信息'''
    # 英雄名
    hname = models.CharField(max_length=20)
    # 性别 默认为False为男性
    hgender = models.BooleanField(default=False)
    # 备注
    hcomment = models.CharField(max_length=200)
    # 属性关联
    hbook = models.ForeignKey('BookInfo')
    # 删除标记
    isDelete = models.BooleanField(default=False)

    class Mate:
        db_table = 'booktest_heroinfo' #元选项，指定模型类的表名，

class AreaInfo(models.Model):
    '''省市查询'''
    # 地区名
    atitle = models.CharField(max_length=20)
    # 自关联属性，代表当前地区的父级地区
    aParent = models.ForeignKey('self',null=True,blank=True)

