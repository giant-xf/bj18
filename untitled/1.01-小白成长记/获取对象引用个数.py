import sys
class  T(object):
    pass
t =T()
print(sys.getrefcount(t))  #调用这个方法时创建一个对象接受这个引用，所以多一个
#比实际个数多一个
