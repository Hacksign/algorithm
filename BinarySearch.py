#!/usr/bin/python2
#-*- coding:utf8 -*-

import sys

def binary_search(number, sorted_array) :
    '''
    作用 : 二分查找一个整形数值在一个有序数组中的插入位置
    @number : int,要插入的数值
    @sorted_array : list,有序数组
    @return : int,插入位置
    '''
    low = 0
    high = len(sorted_array) - 1
    while low <= high :
        half = (high - low) / 2 + low
        if number < sorted_array[half] :
            high = half - 1
        elif number > sorted_array[half] :
            low = half + 1
        else : return half

    return half


if __name__ == '__main__' :
    '''
    usage : ./BinarySearch.py 100
    '''
    array = [5436,1,346,7,43567,4375367,234,546,3,346,3456,2,34,134]
    sorted_array = sorted(list(set(array)))
    index = binary_search(int(sys.argv[1]), sorted_array)
    if int(sys.argv[1]) < sorted_array[index] : new_array = sorted_array[0 : index] + [int(sys.argv[1])] + sorted_array[index :]
    else : new_array = sorted_array[0 : index + 1] + [int(sys.argv[1])] + sorted_array[index + 1 :]
    print index
    print sorted_array
    print new_array
