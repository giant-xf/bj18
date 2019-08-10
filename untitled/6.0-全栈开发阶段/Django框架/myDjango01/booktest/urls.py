from django.conf.urls import  url # 导入url路由配置模块
from booktest import views # 导入视图模块

urlpatterns =[
    # 通过url函数设置url路由配置，首先需要在项目的urls.py中设置
    url(r'^index$',views.index),  # 建立/index与视图之间联系
    url(r'^index2$',views.index2),

    url(r'^books$',views.show_books), # 显示图书信息
    url(r'^books/(\d+)$',views.detail), # 显示英雄信息,将需要传入的参数分组，
]