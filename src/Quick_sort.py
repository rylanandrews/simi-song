# Quick sort function implementation
# The general logic and organization for this code comes from "6 - Sorting" lecture


def partition(arr, lo, hi):
    pivot = arr[hi][2]
    up = lo
    down = hi
    while (up < down):
        for j in (up, hi):
            if arr[up][2] > pivot:
                break
            up += 1
        
        for j in (hi, lo, -1):
            if arr[down][2] < pivot:
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
    if low < high:
        pivot = partition(array2d, low, high)
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

    sortedList = quick_sort(sampleList, 1, len(sampleList))

    print(sortedList)

unit_test()