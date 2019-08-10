'''
test 和 test()区别   函数和变量一样，都是引用，test表示函数名，可以使用a=test ，这样
a()和test()效果一样，
test  #表示函数引用名
test() #表示执行test函数

'''
def f(a,b):

    def test_1(x):
        print(a*x+b)
    return test_1

ln1 =f(1,1)
ln1(2)
ln2 =f(2,5)
ln2(2)
#第一次调用函数时，ln1指向函数，，再次调用时，之前的数据不会清理，
#会重新创建一块内存

#应用在一次函数