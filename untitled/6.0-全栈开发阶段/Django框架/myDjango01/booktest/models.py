from django.db import models

# Create your models here.

class BookInfo(models.Model):
    '''图书类模型'''
    # 图书名称，CharField说明是一个字符串，max_length表示最大长度为20
    btitle = models.CharField(max_length=20)

    # 图书出版日期,DateField说明是一个日期类型
    bpub_date = models.DateField()

    def __str__(self):
        # 返回书名
        return self.btitle



# 英雄人物类
# 英雄名 hname
# 性别 hgender
# 备注 hcomment
# 关系属性 hbook建立图书类和英雄人物一对多关系
class HeroInfo(models.Model):
    '''英雄人物信息'''
    # 英雄名称
    hname = models.CharField(max_length=20)
    # 英雄性别 ,BooleanField说明bool类型，default设置默认值，false代表男
    hgender = models.BooleanField(default=False)
    # 英雄备注
    hcomment = models.CharField(max_length=128)
    #关系属性 hbook建立图书类和英雄人物一对多关系
    # 生成的关系属性对应的表的字段名格式: 关系属性名_id
    hbook = models.ForeignKey('BookInfo')

    def __str__(self):
        # 返回英雄的名字
        return self.hname

