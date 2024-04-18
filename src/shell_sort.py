# Author: Rylan Andrews
# Date: 2024-04-18
# Shell sorts a list of songs

# Credit: COP3530 class notes

def shell_sort(songList):
    n = len(songList)

    gap = int(n / 2)

    # psuedocode (from class notes):
    # while gap > 0
    #   for each array element from position gap to last element
    #       insert where it belongs in subarray
    #   if gap is 2, make 1
    # else gap = gap / 2.2

    # Iterate until no more gap
    while (gap > 0):    

        # Iterate over entire list
        for i in range(gap, n):
            # Compute the indices of the two elements to be compared
            iLeft = i - gap
            iRight = i

            # If out-of-place element found, swap it until it's in proper place (insertion-sort style)
            while (iLeft >= 0 and songList[iRight][1] > songList[iLeft][1]):
                # Swap elements
                temp = songList[iRight]
                songList[iRight] = songList[iLeft]
                songList[iLeft] = temp

                # Increment to next elements
                iLeft = iLeft - gap
                iRight = iRight - gap
        
        # Reduce gap
        gap = int(gap / 2.2)

    return songList

        
def unitTest():
    sampleList = [
        ["song5", 5],
        ["song3", 3],
        ["song6", 6],
        ["song1", 1],
        ["song3", 3],
        ["song8", 8],
    ]

    sortedList = shell_sort(sampleList)
    
    for i in range(len(sortedList)):
        print(sortedList[i][0])

unitTest()