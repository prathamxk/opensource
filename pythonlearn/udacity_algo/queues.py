# line of people standing in front of ice cream shop.
# first in first out structure -  FIFO
# most oldest element comes out first,
# first element - head
# last element - tail
# add element to the tail of the queue - Enqueue
# remove element to the head of the queue - Dequeue
# Peek - only look at the value of head element
# This can be implemented using linked list, with 2 references head and tail.

# Deck - is a generalized version of both stack and queue, you can add / remove elements in either end.

# priority queue - when you add element to a Queue you add additional parameter called priority.
# when you dequeue you remove the element with highest priority. If 2 elements have same highest priority then oldest element gets dequeued first.


"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""

class Queue:
    def __init__(self, head=None):
        self.storage = [head]


    def enqueue(self, new_element):
        self.storage.append(new_element)
        pass

    def peek(self):
        if self.storage == None:
            return None
        else:
            return self.storage[0]

    def dequeue(self):
        # Always remove the first element.
        if self.storage == None:
            return None
        else:
            return self.storage.pop(0)

    
# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print(q.peek())

# Test dequeue
# Should be 1
print(q.dequeue())

# Test enqueue
q.enqueue(4)
# Should be 2
print(q.dequeue())
# Should be 3
print(q.dequeue())
# Should be 4
print(q.dequeue())
q.enqueue(5)
# Should be 5
print(q.peek())