from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^index$',views.index),
    url(r'^showarg(?P<num>\d+)$',views.show_arg),    # ?P<name>给参数命名，必须一致

    url(r'^login$',views.login),    # 登入界面
    url(r'^login_check$',views.login_check),    # 登入校验

    url(r'^login_ajax$',views.login_ajax),  # ajax登入界面
    url(r'^login_ajax_check$',views.login_ajax_check),   # ajax校验页面

    url(r'^set_cookie$',views.set_cookie),   # 设置cookie
    url(r'^get_cookie$',views.get_cookie),  # 获取cookie

    url(r'^set_session$',views.set_session),   # 设置session
    url(r'^get_session$',views.get_session),    # 获取session
    url(r'^clear_session$', views.clear_session),   #删除session

    url(r'^show_reqarg/$', views.show_reqarg),  # get、post提交区别
]
