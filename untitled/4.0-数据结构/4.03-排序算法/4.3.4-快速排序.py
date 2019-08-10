

#快速排序针对的是整个列表，每次传入的必须是整个列表，不同的是每次操作的列表范围不同


#最坏时间复杂度为：O(n^2)
#最优时间复杂度为：O(nlogn)
#稳定性：不稳定

def quick_sort(alist,first,last):
    """快速排序"""
    n = len(alist)
    mid_value = alist[first]
    low = first
    high = last
    if first >= last:
        return
    while low < high :
        #high 左移
        if low < high and alist[high] >= mid_value :
            high -=1
        alist[low] = alist[high]
        #low 右移
        if low < high and alist[low] < mid_value:
            low +=1
        alist[high] = alist[low]
    #退出循环后，low == high 此时让mid_value插进去
    alist[low] = mid_value

    #递归，对low左边的进行排序
    quick_sort(alist,first,low-1)
    #对low右边的进行排序
    quick_sort(alist,low+1,last)

def quick_sort1(alist,first,last):
    n = len(alist)
    #两个游标
    low = first
    high = last

    #用来比较的值
    mid_value = alist[first]

    #控制递归结束
    if low >= high:
        return

    while low < high:
        #higt 左移
        while low < high and alist[high] >= mid_value:
            high -=1
        alist[low] = alist[high]

        while low < high and alist[low] < mid_value:
            low +=1
        alist[high] = alist[low]

    alist[low] = mid_value

    quick_sort1(alist,first,low-1)
    quick_sort1(alist,low+1,last)
if __name__ == '__main__':
    li = [22,33,55,44,34,23,56,11,23]
    print(li)
    #quick_sort(li,0,len(li)-1)
    quick_sort1(li,0,len(li)-1)
    print(li)
