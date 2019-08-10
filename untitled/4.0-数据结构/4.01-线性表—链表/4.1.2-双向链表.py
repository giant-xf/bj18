class Node(object):
    """单链表的节点"""
    def __init__(self,elem):
        #存放数据元素
        self.elem = elem
        #下一个节点的标记
        self.next = None
        #指向前一个节点的游标
        self.prev = None

class DoubleLinkList(object):
    """双链表的实现"""

    def __init__(self, node=None):
        #私有变量来存储 表头
        self.__head = node

    def is_empty(self):
        '''链表是否为空'''
        return self.__head == None

    def length(self):
        '''链表长度'''
        #指针,指针初始化指向位置
        cur = self.__head
        #记数
        count = 0
        while cur != None:
            count +=1
            #将cur后移一个节点
            cur = cur.next
        return count

    def travel(self):
        '''遍历整个链表'''
        cur = self.__head
        while cur != None:
            print(cur.elem,end=" ")
            cur = cur.next
        print("")

    def add(self,item):
        '''链表头部添加元素'''
        node = Node(item)
        if self.__head == None:
            self.__head = node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node
           #顺序不同，代码不同
          #  node.next.prev = node

    def append(self,item):
        '''链表尾部添加元素'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            #将cur.next指向一个封装对象
            cur.next = node
            node.prev = cur

    def insert(self,pos, item):
        '''指定位置添加元素
        :param pos为0开始
        '''
        node = Node(item)
        #pre = self.__head
        cur = self.__head
        count = 0
        if pos <=0: #pos=2
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            while count != pos-1:
                count +=1
                cur = cur.next
            node.next = cur.next
            cur.next = node
            node.next.prev = node
            node.prev = cur

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
        cur = self.__head
      #  pre = None
        if self.__head ==None:
            print("该链表为空表")

        while cur != None:
            #找到节点的数据，然后删除
            if cur.elem == item:
                if cur.prev == None:
                    #删除的数据为第一个数据时
                    self.__head = cur.next
                    if cur.next != None:
                        #判断链表是否只有一个元素
                        cur.next.prev = None
                elif cur.next == None:
                    cur.prev.next = None
                else:
                    #删除数据节点
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                break
            else:
                cur = cur.next
        if self.__head != None and cur == None:
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
            print("不存在:",item)

if __name__ == '__main__':
    ll =DoubleLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(5)
    ll.append(6)
    ll.add(3)
    ll.add(4)
    ll.travel()

    ll.insert(3,7)
    ll.travel()
    ll.insert(-1,8)
    ll.travel()
    ll.insert(10,9)
    ll.travel()

    ll.remove(8)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(7)
    ll.travel()
    ll.remove(100)
    ll.travel()

    ll.search(5)
    ll.search(10)
