# most confusing topic, to understand better go through multiple examples and try to solve them.
# must have a good base condition where the recursion stops, if we don't have a base condition the recursion goes in infinite loop.
# we also must alter the input / variables in order to reach the base condition otherwise it keeps going in infinite loop.
# during recursive call the incomplete calculations are stored in the temporary memory.

"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    # base case 1
    if position == 0:
        return 0
    # base case 2
    elif position == 1:
        return 1
    elif position > 1:
        return get_fib(position-1) + get_fib(position-2)

# Test cases
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))

# fib(0) + fib(1) + fib(2) + fib(3) + fib(4)
# 0         1           1       2       3


# fib(4) -> fib(3) + fib(2)
# fib(3) -> fib(2) + fib(1)
# fib(2) -> fib(1) + fib(0)