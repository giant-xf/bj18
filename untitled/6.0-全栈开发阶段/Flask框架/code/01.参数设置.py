# coding:utf-8

from flask import Flask,current_app,render_template
# import demo

# 创建flask的应用对象
# 魔法变量:__name__表示当前的模块名字
#               模块名，flask以这个模板所在的目录为总目录,默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__,
            static_url_path='/python',  # 访问静态资源的url前缀，默认值为static，输入127.0.0.1:5000/python/index.html时，访问设置的url前缀时，跳转到静态文件下的index文件，不会跳到动态视图。
            static_folder='static',     # 静态文件的目录，默认值为static
            template_folder='templates')   # 访问静态文件的url前缀，默认是static

# app = Flask("__main__")
# app = Flask('asdas')

# 配置参数的使用方式
# 1.使用配置文件
# app.config.from_pyfile('config.cfg')

# 2.使用对象配置参数
class Config(object):
    DEBUG = True
    ITCAST = 'python'
app.config.from_object(Config)

# 3.直接操作config的字典对象
# app.config['DEBUG']=True

# 后面括号相当于url配置
@app.route('/')
def index():
    '''定义视图函数'''
    # 读取配置参数
    # 1.直接从全局对象app的config字典中取值
    # print(app.config.get('ITCAST'))
    # 2.通过current_app获取参数
    print (current_app.config.get('ITCAST'))

    # 没有那些Httprepose这些，直接返回响应体的字符串
    return 'hello flask'

if __name__ == '__main__':
    # 启动flask程序
    # app.run()
    # 可以设置host和port,在app.run中只能设置debug参数
    app.run(host='192.168.1.100',port=5000,debug=True)
