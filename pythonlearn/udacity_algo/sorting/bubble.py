"""In sorting algo 
naive approach - compare each element with other could be too much time consuming
sorting algorithms - memorize their runtime
2 types:
1. in place - no need to copy to another data structure and uses existing data structure and sort the elements.
2. not in place sorting - requires to copy data to another data structure
Trade off - less space or less time, we can mention it in the interview which one we are going to do and why you are selecting it.
more reasons you provide the smarter you seem.
"""

#bubble sort is naive approach - after 1st iteration the largest element moves to the end of the array
# in 2nd iteration 2nd largest element bubbles up hence known as bubble sort
# example: 8 3 1 7 0

# efficiency of algorithms - n-1 * n-1 = n^2 - 2n +1 ~ n^2
# worst and average case - O(n^2)
# best case = O(n)
# no extra data structures, no elements. Same space complexity.

"""Sorting techniques can be tricky—sometimes the best way to understand them is to watch a visual of a sorting algorithm in action again and again.
When I was first learning sorting, I used to check out the Wikipedia page for each sort. 
There's normally some colorful illustration near the top, then a GIF showing the sort in action. 
There are plenty of other visualizations on the World Wide Web—take the time to look around if you need it!"""

def bubbly_sort(unsorted):
    n = len(unsorted)
    for i in range(n-1):
        for j in range(n-i-1):
            if unsorted[j] > unsorted[j+1]:
                unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]

    print(unsorted)

unsorted = [15, 4, 45, 49, 70 , 3, 2, 8, 5]

bubbly_sort(unsorted)
