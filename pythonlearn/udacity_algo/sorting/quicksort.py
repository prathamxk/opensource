# quicksort - one of the most efficient algo.
# pick one of the values in the array at random
# Move all values larger than it to right / above it
# move all values smaller than it to left / below it
# value you initially pick up is called PIVOT
# You continue picking PIVOT in upper and lower section of the array until the whole array is sorted.
# convention says that to use last element as a pivot, 
# in such case if your first element is larger than the pivot you need to move it behind the pivot
# once we encounter a value which is smaller than pivot, compare it with next element in the LHS
# we compare all elements on the left hand side and make sure they are smaller than pivot.
# now we need to select a new pivot on the left hand side and follow same process on the left hand side
# simillarly we need to select new pivot on the right hand side and follow same process on the right hand side

# efficiency of Qsort.
# worst case of Qsort is O(n^2) - partially sorted array is worst case scenario for the quick sort
# for average and best case scenario its O(n*log(n))
# We can do optimizations for quick sort.
# 1. Configure the program in a way that it runs both halves at the same time.
# 2. instead of selecting last element as a pivot you can use median of last few elements as a pivot for faster execution.
# space complexity is constant as we are doing in placer sorting O(n)


"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
"""def quicksort(array):
    # find the length of the array
    n = len(array)
    # find the pivot
    pivot = array[n-1]
    # compare pivot with all elements in the array and swap
    count = 1
    for element in array:
        if element > pivot:
            # store previous element of pivot to temp
            temp = array[n-count-1]
            # move pivot 1 left of its current position
            array[n-count-1] = pivot
            array[n-count] = element
            element = temp
            if count==2:
                break
            count+=1
    
    return array"""

def partition(array, low, high):
 
    # choose the rightmost element as pivot
    pivot = array[high]
 
    # pointer for greater element
    i = low - 1
 
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
# function to perform quicksort
 
 
def quicksort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pivot = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quicksort(array, low, pivot - 1)
 
        # Recursive call on the right of pivot
        quicksort(array, pivot + 1, high)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
size = len(test)
quicksort(test, 0, size-1)

print(test)
## pivot = 14
# iteration 1 : 21, 4, 1, 3, 9, 20, 25, 6, 14, 21
# iteration 2 : 6, 4, 1, 3, 9, 20, 25, 15, 21, 21
