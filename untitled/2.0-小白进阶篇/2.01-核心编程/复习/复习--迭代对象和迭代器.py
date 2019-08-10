from collections import *
#判断可迭代对象
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance((),Iterable))
print(isinstance('asd',Iterable))
print(isinstance((x*2 for x in range(5)),Iterable))
print(isinstance(100,Iterable))
print('------------------------------')
#判断是否是迭代器
print(isinstance([],Iterator))
print(isinstance((),Iterator))
print(isinstance({},Iterator))
print(isinstance((x*2 for x in range(5)),Iterator))
print(isinstance([x*2 for x in range(5)],Iterator))
print('------------------------------')
#将可迭代对象转换成迭代器
print(isinstance(iter([]),Iterator))
print(isinstance(iter({}),Iterator))
print(isinstance(iter([x*2 for x in range(5)]),Iterator))

'''
总结：
凡是可作⽤于 for 循环的对象都是 Iterable 类型；
凡是可作⽤于 next() 函数的对象都是 Iterator 类型
集合数据类型如 list 、 dict 、 str 等是 Iterable 但不是 Iterator ，不过可
以通过 iter() 函数获得⼀个 Iterator 对象。
'''



