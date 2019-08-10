from django.db import models

# Create your models here.


class AreaInfo(models.Model):
    '''省市查询'''
    # 地区名
    atitle = models.CharField(max_length=20)
    # 自关联属性，代表当前地区的父级地区
    aParent = models.ForeignKey('self',null=True,blank=True)



class PicTest(models.Model):
    '''上传图片'''
    goods_pic = models.ImageField(upload_to='booktest')

    def __str__(self):
        return self.goods_pic






