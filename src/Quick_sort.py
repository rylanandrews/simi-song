# Quick sort function implementation
# The general logic and organization for this code comes from "6 - Sorting" lecture

import sys

#sys.setrecursionlimit(1000000)


def partition(arr, lo, hi):
    pivot = arr[hi][1]
    up = lo
    down = hi
    while (up < down):
        for j in range(up, hi-1):
            if arr[up][1] > pivot:
                break
            up += 1
        
        for j in range(hi, lo+1, -1):
            if arr[down][1] < pivot:
                break
            down -= 1
        
        if up < down:
            #swap arr[up] and arr[down]
            temp = arr[up]
            arr[up] = arr[down]
            arr[down] = temp
            
    #swap arr[lo] and arr[down]
    temp = arr[lo]
    arr[lo] = arr[down]
    arr[down] = temp
    return down


def quick_sort(array2d, low, high):
    # Stuff
    sortedArray = ["title", 0] * (high - low)
    if low < high:
        pivot = partition(array2d, low, high)
        sortedArray[low:pivot-1] = quick_sort(array2d, low, pivot-1)
        sortedArray[pivot+1:high] = quick_sort(array2d, pivot+1, high)
    return sortedArray

def unit_test():
    sampleList = [
        ["song5", 5],
        ["song3", 3],
        ["song6", 6],
        ["song1", 1],
        ["song3", 3],
        ["song8", 8],
    ]

    sortedList = quick_sort(sampleList, 0, len(sampleList)-1)

    print(sortedList)

unit_test()