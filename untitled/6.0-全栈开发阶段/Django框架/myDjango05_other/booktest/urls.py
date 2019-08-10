
from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^static_test$',views.static_test),    # 显示图片
    url(r'^index$',views.index),     #显示首页

    url(r'^show_load$',views.show_load), # 显示上传文件页面
    url(r'^upload_handle$',views.upload_handle),  # 上传图片处理

    url(r'^show_area(?P<pindex>\d*)$',views.show_area),    # 显示省级信息

    url(r'^areas$',views.areas),    # 显示省市县下拉框
    url(r'^prov$',views.prov),  # 获取省级信息
    url(r'^city(\d+)$',views.city),  # 获取省的相应市级信息
    url(r'^dis(\d+)$',views.dis), # 获取市下面的县级信息
]
