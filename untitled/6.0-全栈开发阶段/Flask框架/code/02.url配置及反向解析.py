# coding:utf-8

from flask import Flask,redirect,url_for
# import demo

# 创建flask的应用对象
# 魔法变量:__name__表示当前的模块名字
#               模块名，flask以这个模板所在的目录为总目录,默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__)
# 后面括号相当于url配置
@app.route('/')
def index():
    '''定义视图函数'''
    # 没有那些Httprepose这些，直接返回响应体的字符串
    return 'hello flask'

# 通过methods限制访问方式
@app.route('/post_only', methods=["POST",'GET'])
def post_only():
    return 'post only page'

# 和Django一样，访问地址是根据url配置的先后顺序,若想强制改变，是有后面的视图函数，则可以改变它们的访问方式，
@app.route('/hello', methods=['POST'])
def hello():
    return 'hello 1'
@app.route('/hello', methods=['GET'])
def hello2():
    return 'hello 2'

# 给一个视图配置多个url
@app.route('/hi1')
@app.route('/hi2')
def hi():
    return 'hi page'

# 地址的重定向
@app.route('/login')
def login():
    # url = '/'
    # url(r'/index',index, name='index')
    # 使用url_for函数进行反向解析,视图名即为url的name
    url = url_for('index')
    return redirect(url)


if __name__ == '__main__':
    # 启动flask程序
    # 显示出配置的所有的url
    print (app.url_map)
    app.run(debug=True)
