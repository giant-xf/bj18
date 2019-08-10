
from django.conf.urls import url
from booktest import views
urlpatterns = [
    url(r'^index2$',views.index, name='index'),

    url(r'^temp_val$',views.temp_val),   # 模板变量
    url(r'^temp_tags$',views.temp_tags),    # 模板标签
    url(r'^temp_filter$',views.temp_filter),    # 模板过滤器

    url(r'^login$',views.login),    # 显示登入界面
    url(r'^login_check$',views.login_check),     # 密码校验
    url(r'^change_pwd$',views.change_pwd),  # 显示密码修改页面
    url(r'^change_pwd_action$',views.change_pwd_action),    # 显示密码修改成功页面

    url(r'^verify_code$',views.verify_code),     # 显示验证码

    url(r'^url_reverse$',views.url_reverse),  # url反向解析页面
    url(r'^show_args/(\d+)/(\d+)$',views.show_args, name='show_args'),    #位置参数的url反向解析
    url(r'^show_kwargs/(?P<c>\d+)/(?P<d>\d+)$',views.show_kwargs, name='show_kwargs'),

    url(r'^a_url_reverse$',views.a_url_reverse),  # 重定向url反向解析

]
