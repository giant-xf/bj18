
# j = 0
# li = [11,      33,55,44,34,23,56,22]
#
# j = 1
# li = [11,22,      55,44,34,23,56,33]
#
# j = 2
# i = [11,22,33,      44,34,23,56,55]

#将后面的依次与前面的最大位置的数进行对比，然后将后面小的放在前面，大的放在后面位置,进行交换
#只需要对比n-1次
#与插入算法不同的是，插入算法是将后面的依次插入前面合适的位置，将后面的依次与前面的比较

#最坏时间复杂度为O(n^2)
#最优间复杂度为O(n^2)
#稳定性：不稳定
def select_sort(alist):
    """选择排序"""
    n = len(alist)

    for j in range(n-1):
        #控制循环的趟数
        min_index = j
        for i in range(j+1,n):
            #遍历剩下的区域
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]
        print(j,alist)


if __name__ == '__main__':
    li = [22,33,55,44,34,23,56,11]
    print(li)
    select_sort(li)
    print(li)
