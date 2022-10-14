""" Split the whole array into small and then build it back after sorting.
This methodology is called divide and conquer
1. break up the array into small elements.
2. Merge them back after sorting

Example:

8, 3, 1, 7, 0, 10, 2

Level 1 - breakup the array into small arrays of single element
8   3   1   7   0   10   2

Level 2 - merge them back into small arrays of 2 elements per array and sort within
8   1, 3    0,7    2,10

Level 3 - merge them back into little big array of 3 / 4 element by first sorting. 
Compare first 2 elements of 2 arrays and write smallest number in new array, 
then compare first element with 2nd element and write smallest number in new array,
finally write remaining number last in the new array

1, 3, 8     0, 2, 7, 10

Level 4 - Start comparing first elements in 2 arrays.

0, 1, 2, 3, 7, 8, 10
"""

# Time efficiency - each array takes 1 less number of comparison than the size of the array.
# ex. For array size 7 it takes 6 comparisons, for array size 6 it takes 5 comparisons and so on.
# to make things easier we need to use "Approximation" - 
# There are 2 important aspects we need to consider
#  1. comparison - comparing elements with each other
#  2. iterations - how many times we are going through all the elements.
# result table
#   Array size  1   2   3   4   5   6   7   8   9
#   Iterations  0   1   2   2   3   3   3   3   4
#  time complexity O(n*log(n)) it is better than On^2
#  Auxilary space for bubble sort was constant or O(n)
#  Space complexity is worse than bubble sort

from ast import withitem


def merge_array(arr, l, m, r):
    # find the ranges
    # mid - low + 1
    n1 = m - l + 1
    # high - mid
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # copy data to temp arrays L & R
    for i in range(0, n1):
        L[i] = arr[l + i]

    # copy data to right side 
    for j in range(0, n2):
        R[i] = arr[m + 1 + j]

    # merge the temp arrays back into arr[l..r]
    i = 0   # initial index of first subarray
    j = 0   # initial index of 2nd subarray
    k = l   # initial index of merged subarray

    while i <n1 and j <n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i +=1
        else:
            arr[k] = R[j]
            j +=1
        k += 1
    # copy the remaining element of L[], if there are any
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

    # copy the remaining elements of R[], if there are any
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
    # l is for left index and r is right index of the subarray of arr to be sorted.

def merge_sort(arr, l, r):
    
    if l < r:
        m = l+(r-1)//2
    
        # divide array into 2 sections using recursive function
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)

        # merge arrays 
        merge_array(arr, l, m, r)


merge_unsorted = [8, 3, 1, 7, 0, 10, 2]
n = len(merge_unsorted)
for i in range(n):
    print("%d" % merge_unsorted[i], end=" ")

merge_sort(merge_unsorted, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % merge_unsorted[i],end=" ")

