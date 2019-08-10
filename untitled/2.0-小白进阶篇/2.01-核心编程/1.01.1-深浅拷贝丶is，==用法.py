import copy

# is和 == 的用法
a = [1,2,3]    #元组与数组同理一样
b =[1,2,3]
a1=a
print(a==b,a is b,id(a),id(b)) #引用的是两个不同的地址的数据
print(a ==a1,a is a1,id(a),id(a1)) #a,a1引用的同一个内存的数据
print('-'*30)
c =1000000
c1 =-10
d =1000000
d1 =-10
print(c==d,c is d)
print(c1==d1,c1 is d1)  #表明在一定的范围内才会引用同一片地址
print('-'*30)
#浅拷贝 和深拷贝
#浅拷贝
a =[1,2,3]
b =a      #浅拷贝，引用同一份地址
print(a==b,a is b,id(a),id(b))
print('-'*30)
#深拷贝
a =[1,2,3] #int,str,列表,字典,集合,都行
a =(1,2,3) #元组深拷贝不同
#a =100
#a={'name':1,(1,2):'w'}
b  =copy.deepcopy(a)    #深拷贝，直接拷贝一份新的数据，用b来引用
print(a==b,a is b,id(a),id(b))
print('-'*30)

#deepcopy 和copy的区别
#deepcopy
a =[1,2,3]
b =[4,5,6]
c =[a,b] #列表的嵌套
#c =(a,b) #元组也一样
d =copy.deepcopy(c)
print(id(c),id(d))
a.append(11)
print(c[0],d[0])  #说明重新申请了一份内存，且是递归拷贝
#deepcopy 深拷贝可以递归拷贝，都是重新拷贝一份内存
print('-'*30)
#copy
a =[1,2,3]
b =[4,5,6]
c =[a,b] #列表的嵌套
d =copy.copy(c)
print(id(c),id(d))  #深拷贝了第一层(重新创了内存)
a.append(11)
print(c[0],d[0])  #没有深拷贝第二层(没有重新创内存)
#copy拷贝可变类型只能深拷贝第一层，第二层没有深拷贝，
c =(a,b)
d =copy.copy(c)
print(id(c),id(d))   #内存地址相同，浅拷贝
#copy拷贝不可变类型直接浅拷贝
#***copy可以判断可变和不可变类型