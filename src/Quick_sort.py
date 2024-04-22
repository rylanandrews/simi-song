# Quick sort function implementation

# Credit "COP 3530" lecture "6 - Sorting"


import sys

#sys.setrecursionlimit(1000000)


def partition(arr, lo, hi):
    # Set pivot as lowest element, initialize up as lowest, and down as highest
    pivot = arr[lo][1]
    up = lo
    down = hi
    # 
    while (up < down):
        # Moves up up the list until it finds a value less than pivot
        for j in range(up, hi):
            if arr[up][1] < pivot:
                break
            up += 1
        
        # Moves down down the list until it finds a value greater than pivot
        for j in range(down, lo, -1):
            if arr[down][1] > pivot:
                break
            down -= 1
        
        # Swaps up and down if necessary
        if up < down:
            #swap arr[up] and arr[down]
            temp = arr[up]
            arr[up] = arr[down]
            arr[down] = temp
    
    # Swap pivot with arr[down], placing pivot in correct location
    temp = arr[lo]
    arr[lo] = arr[down]
    arr[down] = temp
    return down


def quick_sort(array2d, low, high):
    # As long as this quick_sort() call is valid, partition and
    # recursively call quick_sort() on sub-lists
    if low < high:
        # Places pivot in correct location, and returns where that location is
        pivot = partition(array2d, low, high)
        # Recursively calls quick_sort() on sub-lists above and below the recently placed pivot
        quick_sort(array2d, low, pivot-1)
        quick_sort(array2d, pivot+1, high)

def unit_test():
    sampleList = [
        ["song5", 5],
        ["song3", 3],
        ["song6", 6],
        ["song1", 1],
        ["song3", 3],
        ["song8", 8],
    ]

    quick_sort(sampleList, 0, len(sampleList)-1)

    print(sampleList)

#unit_test()
