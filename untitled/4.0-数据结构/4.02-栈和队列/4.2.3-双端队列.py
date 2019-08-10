class Queue(object):
    #创建一个空的队列
    def __init__(self):
        #存储列表的容器
        self.__list = []

    def add_rear(self,item):
        #往队列中添加一个item元素
        self.__list.append(item)
        #头插入，头出来,时间复杂度 O(n)
        #self.__list.insert(0,item)

    def add_font(self,item):
        #往队列中添加一个item元素
        self.__list.insert(0,item)

    def remove_font(self):
        #从队列头部删除一个元素
        #return self.__list.pop()
        #头删除 时间复杂度 O(n)
        return self.__list.pop(0)

    def remove_rear(self):
        #从队列头部删除一个元素
        return self.__list.pop()

    def is_empty(self):
        #判断一个队列是否为空
        return not self.__list

    def size(self):
        #返回队列的大小
        return len(self.__list)

    def dayin(self):
        print(self.__list)

if __name__ == '__main__':
    s = Queue()
    print(s.is_empty())
    s.add_font(1)
    s.add_font(2)
    s.add_rear(3)
    s.dayin()
                #[2,1,3]
    print(s.size())
    print(s.remove_font())
    print(s.remove_rear())
    s.dayin()

