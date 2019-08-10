#希尔排序的整体思路还是插入排序
#希尔排序主要是将其分成多组，以gap为间隔，然后第一次排完后继续gap//2继续分组
#最坏时间复杂度为：O(n^2)
#最优时间复杂度为：O(n^1.3)
#稳定性：不稳定
def shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    gap = n//2
    #第一次间隔为n//2，第二次为.....，直到所有为一组时
    while gap > 0:
        #利用每次的挨个移动，做到依次将每个组内之间进行比较
        for i in range(gap,n):
            #i = [gap,gap+1,gap+2,gap+3....n-1]
            while i > 0:
                #将其分组以后，内层循环控制每组之间的数据交换(插入排序算法)
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -=gap
                else:
                    break
            #print(alist)
        gap //=2

def shell_sort1(alist):
    n = len(alist)

    gap = n//2

    while gap >0:
        for i in range(gap,n):
            #i =[gap,gap+1,gap+2,...n-1]
            if alist[i] > alist[i-gap]:
                alist[i], alist[i-gap] = alist[i-gap], alist[i]
                i +=1
            else:
                break
        gap = gap//2
if __name__ == '__main__':
    li = [22,33,55,44,34,23,56,11,23]
    print(li)
    shell_sort(li)
    print(li)