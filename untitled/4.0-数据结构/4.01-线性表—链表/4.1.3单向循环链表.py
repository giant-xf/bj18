class Node(object):
    """单链表的节点"""
    def __init__(self,elem):
        #存放数据元素
        self.elem = elem
        #下一个节点的标记
        self.next = None

class SingleLinkList(object):
    """单向循环链表的实现"""

    def __init__(self, node=None):
        #私有变量来存储 表头
        self.__head = node
        if node:
            #如果开始传入的不是空链表，而是一个结点的话需要设置回环
            node.next = node

    def is_empty(self):
        '''链表是否为空'''
        return self.__head == None

    def length(self):
        '''链表长度'''
        #指针,指针初始化指向位置
        cur = self.__head
        if self.is_empty():
            return
        #记数
        count = 1
        while cur.next != self.__head:
            count +=1
            #将cur后移一个节点
            cur = cur.next
        return count

    def travel(self):
        '''遍历整个链表'''
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem,end=" ")
            cur = cur.next
        print(cur.elem,)

    def add(self,item):
        '''链表头部添加元素'''
        node = Node(item)
        cur = self.__head
        if self.__head == None:
            self.__head = node
            node.next = node
        else:
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head
            self.__head = node

    def append(self,item):
        '''链表尾部添加元素'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            #将cur.next指向一个封装对象
            cur.next = node
            node.next = self.__head

    def insert(self,pos, item):
        '''指定位置添加元素
        :param pos为0开始
        '''
        node = Node(item)
        pre = self.__head
        count = 0
        if pos <=0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            while count < (pos-1):
                count +=1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self,item):
        '''删除节点'''
        # node = Node(item)
        # cur = self.__head
        # pre = self.__head
        # count = 0
        # if self.is_empty():
        #     print( "链表为空")
        # elif cur.elem == node.elem:
        #     self.__head = cur.next
        # else:
        #     while cur.next != None:
        #         count +=1
        #         cur = cur.next
        #         if pre.elem == item:
        #             pre.next = cur.next
        #             break
        #         pre = pre.next
        #     if count == self.length()-1:
        #         print("链表中没有这个数据")
        if self.is_empty():
            print("该链表为空表")
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            #找到节点的数据，然后删除
            if cur.elem == item:
                #删除数据节点
                #先判断是否是头结点
                if pre == None:
                    #找到尾结点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    pre.next = cur.next
                #cur.next = None
                return
            else:
                pre = cur
                cur = cur.next
        if cur.elem == item :
            #if cur.next != None:
                if cur == self.__head :
                    self.__head = None
                else:
                    pre.next = self.__head

        if self.__head != None and cur.next == self.__head and cur.elem != item:
            print("没有该数据")

    def search(self,item):
        '''查找节点是否存在'''
        cur = self.__head
        while cur != None:
            if  cur.elem == item:
                print("存在",item)
                break
            cur = cur.next
        if cur == None:
            print("不存在")

if __name__ == '__main__':
    ll =SingleLinkList(Node(20))
   # print(ll.is_empty())
   # print(ll.length())
   # ll.travel()

    ll.add(1)
    ll.add(2)
    ll.travel()
    print(ll.length())

    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.travel()

    ll.insert(-1,100)
    ll.travel()
    ll.insert(10,200)
    ll.travel()
    ll.insert(4,300)
    ll.travel()

    ll.remove(100)
    ll.travel()
    ll.remove(200)
    ll.travel()
    ll.remove(300)
    ll.travel()


