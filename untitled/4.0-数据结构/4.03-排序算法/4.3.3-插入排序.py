
#插入算法是将后面的依次插入前面合适的位置，将后面的依次与前面的比较


#最坏时间复杂度为：O(n^2)
#最优时间复杂度为：O(n)
#稳定性：稳定
def insert_sort(alist):
    """插入排序"""
    n = len(alist)

    for i in range(n):
        #控制趟数
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -=1
            else:
                break
        print(alist)

if __name__ == '__main__':
    li = [22,33,55,44,34,23,56,11]
    print(li)
    insert_sort(li)
    print(li)
