def selfadd(a):
    """自增"""
    a +=a

list=[1,2]
selfadd(list)
print(list)

tuple =(1,2)
selfadd(tuple)
print(tuple)

num =1
selfadd(num)
print(num)


#可变类型可以自增，不可变类型不可以自增