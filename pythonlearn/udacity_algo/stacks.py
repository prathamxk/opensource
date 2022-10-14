# if you need easy access to top element use stack. or order in which you save the elements matter.
# add eleemnts is called push
# take element out is POP
# push and pop takes same time O(1)
# LIFO - Last in first out 
# linked list can be used to make stack. only keep track of front element / top element / last element in the linked list.

"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""

from operator import truediv


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
    # only for debug
    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        if self.head == None:
            self.head = new_element
        else:
            new_element.next = self.head
            self.head = new_element
        pass

    def delete_first(self):
        
        if self.isEmpty():
            return None
        current = self.head
        if self.head:
            self.head = self.head.next
        current.next = None
        return current
        "Delete the first (head) element in the LinkedList as return it"        

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)
        # only for debugging 
        # self.ll.print_list()
        pass

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first()
        pass
        

    
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop())
stack.push(e4)
print(stack.pop().value)