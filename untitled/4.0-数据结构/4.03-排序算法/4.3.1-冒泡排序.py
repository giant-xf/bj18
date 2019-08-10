
#最坏时间复杂度为O(n^2)
#最优时间复杂度为O(n)
#稳定性：稳定
def bubble_sort_down(alist):
    '''冒泡排序升序法'''
    n =len(alist)
    for j in range(n-1):
        #控制趟数
        count = 0
        for i in range(n-1-j):
            #比较的次数
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
                count +=1
        if count == 0:
            return
        print(j,alist)

def bubble_sort_up(alist):
    """冒泡排序倒序法"""
    n = len(alist)
    for j in range(n-1):
        for i in range(0,n-1):
            #内层循环代表每趟比较次数
            if alist[i] < alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
        print(j,alist)

if __name__ == '__main__':
    li = [22,33,55,44,34,23,56,11,23]
    print(li)
    #bubble_sort_down(li)
    bubble_sort_up(li)
    print(li)