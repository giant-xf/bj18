
# 自定义过滤器
# 过滤器就是python函数
from django.template import Library

# 创建一个Library对象
register = Library()

@register.filter
def mod(num):
    '''判断num是否为偶数'''
    return num%2 == 0