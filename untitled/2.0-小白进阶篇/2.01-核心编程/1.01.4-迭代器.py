from collections import Iterator   #判断是否是迭代器对象
from collections import Iterable  #判断是否可以迭代
print('-----判断是否是迭代器对象')
print(isinstance([],Iterator))
print(isinstance((),Iterator))
print(isinstance((i for i in range(10)),Iterator))
print(isinstance('abc',Iterator))

print('-----判断是否可以迭代')
print(isinstance([],Iterable))
print(isinstance((),Iterable))
print(isinstance('abc',Iterable))
print(isinstance(100,Iterable))

print('----iter()函数可以将一个可迭代的非迭代对象转换成可迭代')

print(isinstance(iter([]),Iterator))
print(isinstance(iter(()),Iterator))
#iter()函数可以把 list 、 dict 、 str 等 Iterable 变成 Iterator

#print(isinstance(iter(100),Iterator)) #不能将不可迭代的转换成可迭代的
#
#生成器一定是迭代器,迭代器不一定是生成器
#⽣成器都是 Iterator 对象，但 list 、 dict 、 str 虽然是 Iterable ，
# 却不是Iterator 。

'''
总结:
    凡是可作⽤于 for 循环的对象都是 Iterable 类型；
    凡是可作⽤于 next() 函数的对象都是 Iterator 类型
    集合数据类型如 list 、 dict 、 str 等是 Iterable 但不是 Iterator ，不过可
    以通过 iter() 函数获得⼀个 Iterator 对象
'''