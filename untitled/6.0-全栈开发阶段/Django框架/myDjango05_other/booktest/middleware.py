from django.http import HttpResponse


# class BlockedIPSMiddleware(object):
#     '''中间件类'''
#     # 禁止访问的ip名单
#     EXCLUDE_IPS = ['127.0.0.1']
#     def process_view(self,request,view_func,*args,**kwargs):
#         # 获取浏览器ip地址
#         user_ip = request.META['REMOTE_ADDR']
#         if user_ip in BlockedIPSMiddleware.EXCLUDE_IPS:
#             return HttpResponse('<h1>禁止访问</h1>')
#         else:
#             return view_func(request, *args, **kwargs)
#

class my_mid:
    '''项目运行时需要运行的中间件类'''

    #初 始化：无需任何参数，服务器响应第一个请求的时候调用一次，用于确定是否启用当前中间件。
    def __init__(self):
        print ('--------------init')

    # 处理请求前：在每个请求上，request对象产生之后，url匹配之前调用，返回None或HttpResponse对象。
    def process_request(self,request):
        print ('--------------request')
        # return HttpResponse('ok')

    # 处理视图前：在每个请求上，url匹配之后，视图函数调用之前调用，返回None或HttpResponse对象。
    def process_view(self,request, view_func, *view_args, **view_kwargs):
        print ('--------------view')

    # 处理响应后：视图函数调用之后，所有响应返回浏览器之前被调用，在每个请求上调用，返回HttpResponse对象。
    def process_response(self,request, response):
        print ('--------------response')
        return response
