#!/usr/bin/python2
#-*- coding:utf8 -*-

def quick_sort(A, low, high):
    '''
    快速排序算法实现
    @A : array,未排序过的数组
    @low : 开始排序的低位
    @high : 结束排序的高位
    @return : 无
    @参考资料 : http://developer.51cto.com/art/201403/430986.htm
    '''
    if low >= high : return
    key = A[low]
    i = low + 1
    j = high
    while i < j :
        while i < j and  A[j] >= key : j -= 1
        while i < j and A[i] <= key : i += 1
        tmp = A[i]
        A[i] = A[j]
        A[j] = tmp
    A[low] = A[i]
    A[i] = key
    quick_sort(A, low, i - 1)
    quick_sort(A, i+ 1, high)

if __name__ == '__main__' :
    unsorted_array = [2,9,1,7,7,5,6,3,4,0,8]
    quick_sort(unsorted_array, 0, len(unsorted_array) - 1)
    print unsorted_array
