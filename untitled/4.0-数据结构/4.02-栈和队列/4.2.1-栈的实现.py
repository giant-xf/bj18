class Stack(object):
    #创建一个空的栈
    def __init__(self):
        self.__list = []

    def push(self,item):
        #添加一个新的元素item到栈顶
        self.__list.append(item)

    def pop(self):
        #弹出栈顶元素
        return self.__list.pop()

    def peek(self):
        #返回栈顶元素
        if self.is_empty():
            return None
        else:
            return self.__list[-1]

    def is_empty(self):
        #判断栈是否为空
        return not self.__list

    def size(self):
        #返回栈的元素个数
        return len(self.__list)


if __name__ == '__main__':
    s = Stack()
    print(s.is_empty())
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.is_empty())
    print(s.size())
    print(s.peek())
    print(s.pop())
    print(s.pop())
    print(s.pop())

