
#在函数内部再定义⼀个函数，并且这个函数⽤到了外边函数的变量，
# 那么将这个函数以及⽤到的⼀些变量称之为闭包
def test(number):

    def test_in(number_in):

        print("test_in 函数传入的值为:",number_in)

        return number_in+number

    return test_in

ret =test(20) #获得里面test_in函数对象
print(ret(200))


#描述一条直线函数
def line_conf(a,b):
    def line(x):
        return a*x+b
    return line

ret =line_conf(2,3)
print(ret(11))



