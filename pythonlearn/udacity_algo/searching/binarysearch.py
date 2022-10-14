# searching a number or an element in a given sorted array.
# if we keep on comparing each element from start or from the end it will take lot of time.
# considering the array is sorted we can find the middle of an array and check if its bigger or smaller than our pivot element.
# if its bigger we can count length of middle till end of an array and again divide by 2 and see if pivot is bigger or smaller than next middle number.

# efficiency of an algorithm
# exceptional case can come where we have 2 numbers in the middle or the numbers in an array count is even.
# In such case better to take lower number from the middle numbers.

# if you want to make sure you're checking for the worst case take any bigger number than all elements and try to find in first half of an array
# for array size of 8 there are 4 iterations required.
# every time the size of an array is doubled it takes an extra iteration to pass through it. for instance, 2^0, 2^1, 2^2, 2^3 when the number of iterations are getting added by 1
# the time efficiency becomes O(2^n + 1), considering logarithms we can convert into O(log n + 1). Adding or removing a constant 1 doesn't change value of log(n) much
# in Comp science it is safe to assume that any log(n) can be considered to the base 2 so log to base 2 can be simply used as O(log(n))

# general rule of thumb is to remember basic algorithm efficiencies like binary search and so on, but in case of unknown algorithm you will need to create a result table is one of the best thing
# it helps you notice patterns within array size and iterations etc.
# Never say, that haven't seen the algorithm, try to make results table and find the efficiency based on the result table rather.

"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

from operator import indexOf


def binary_search(input_array, value):
    low = 0
    high = len(input_array) - 1
    mid = 0

    while low <= high:
        mid = (high+low)//2

        if value < input_array[mid]:
        # recursive case 2 - search lower half
            high = mid - 1
        elif value > input_array[mid]:
        # recursive case 1 - search higher half
            low = mid + 1
        else:
            # base case 1 (element found!!)
            return mid
    else:
        # base case 2 (if element not found)
        return -1

test_list = [1,3,9,11,15]
test_val1 = 11

"""test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15"""
print(binary_search(test_list, test_val1))
#print(binary_search(test_list, test_val2))

# search for bin_s(arr, 11) -> rec case 1  bin_s(arr, 11)
