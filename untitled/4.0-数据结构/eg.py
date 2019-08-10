class Node(object):
    """单链表的节点"""
    def __init__(self,elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    """单链表的实现"""
    def __init__(self):
        self.__head =None

    def is_empty(self):
        """判断是否为空"""
        return self.__head == None

    def length(self):
        '''链表的长度'''
        #指针/游标指向表头
        cur = self.__head
        #计数
        count = 0
        while cur != None:
            count +=1
            cur  = cur.next
        return count

    def travel(self):
        """链表的遍历"""
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next

    def add(self,item):
        """链表表头添加数据"""
        node = Node(item)
        if self.__head == Node:
            self.__head = node
        else:
            node.next = self.__head
            self.__head = node


    def append(self,item):
        """链表尾部添加数据"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

if __name__ == '__main__':
    ll =SingleLinkList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)
    #ll.travel()

    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.append(8)
    ll.travel()

    # print(ll.is_empty())
    # print(ll.length())
    #
    # ll.append(1)
    # print(ll.is_empty())
    # print(ll.length())
    #
    # ll.append(2)
    # ll.append(3)
    # ll.append(4)
    # ll.append(5)
    # ll.append(6)
    # ll.travel()
