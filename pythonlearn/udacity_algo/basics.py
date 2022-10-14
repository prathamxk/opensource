# basics.py

"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""

from tkinter import E, Y


class Classy(object):

    def __init__(self):
        self.items = []

    def addItem(self, itemname):
        self.items.append(itemname)

    def getClassiness(self):
        classiness = 0
        for item in self.items:
            classiness = classiness + self.getVal(item) 
        return classiness

    def getVal(self, item):
        if item == "tophat":
            return 2
        elif item == "bowtie":
            return 4
        elif item == "monocle":
            return 5
        else:
            return 0

# Test cases
me = Classy()

# Should be 0
#  print(me.getClassiness())

me.addItem("tophat")
# Should be 2
# print(me.getClassiness())

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
# print(me.getClassiness())

me.addItem("bowtie")
# Should be 15
#print(me.getClassiness())

# print(me.items)

def show_excitement():
    # Your code goes here!
    return ("I am super excited for this course! " * 5)

#print(show_excitement())

# efficiency is in terms of space and time. How much time taken it takes to execute the program.
# can rely on creativity.
# series of steps = algorithm
# big o notation O(n), where n indicates length of an input to your function
# example of cipher
# A -> Y
# B -> E
# C -> S 
# to convert the string of length n = 10 it will need to go through 29(10)+2 for 1 million letters it will be approx 29 million

# approximations - depending on situation and the data structures things change. O(n), in interview we should be able to show that we care about efficiency.
# Some numbers of computations must be performed for EACH letter in the input. Worst case scenario keeps upper bound which we should always consider.

# Space efficiency
# when you copy a same string 3 times in different variables it makes the space efficiency O(3n)

"""input manatees: a list of "manatees", where one manatee is represented by a dictionary
a single manatee has properties like "name", "age", et cetera
n = the number of elements in "manatees"
m = the number of properties per "manatee" (i.e. the number of keys in a manatee dictionary)"""

def example1(manatees):
    for manatee in manatees:
        print(manatee['name'])
# O(n)

def example2(manatees):
    print(manatees[0]['name'])
    print(manatees[0]['age'])
# O(1)

def example3(manatees):
    for manatee in manatees:
        for manatee_property in manatee:
            print(manatee_property, ": ", manatee[manatee_property])
# O(n*m)

def example4(manatees):
    oldest_manatee = "No manatees here!"
    for manatee1 in manatees:
        for manatee2 in manatees:
            if manatee1['age'] < manatee2['age']:
                oldest_manatee = manatee2['name']
            else:
                oldest_manatee = manatee1['name']
    print(oldest_manatee)
# O(n2)

# collections = books, toys etc., doesn't have specific order / inherent order,
# there are many data structures which are extensions of the collections.

# lists = group of things and objects in it have an order. No fixed length, based on the length different programming language.

# arrays = most common implementation, list with few added rules and things are in order, array has a set size when initialized in certain languages,
# each array has a location called "index", index denotes a number associated with each place in an array, it starts at 0.
# array is very useful when we have to find an element at the middle of a list and we know where we won't have to go beyond certain limits.
# Insertion and deletion can be messy, insertion at the end / start is easy,
# but if it needs to be in middle its difficult as you will need to left shift or right shift all other elements after or before the added or deleted elements.
# Python has an interesting data stucture called a "list" that is much more than a mere list. Behind the scenes a Python list is built as an array.

# example, inserting into a list is easy however inserting into an array is O(n), since you may need to shift elements to make space for the one you're inserting.
# Python is a "higher level" programming language, so you can accomplish a task with little code. However,
# there's a lot of code built into the infrastructure in this way that causes your code to actually run much more slowly than you'd think.
# what is the runtime of len() function in python - O(1)

# linked list - each element is connected to next element with reference. Why linked list ? adding and removing elements is easier than array.
# in array we store number as index, in linked list we store reference of next linked list item which is basically memory reference / address.
# insertion takes constant time similar for deletion.
# in doubly linked list, you can traverse the list in both directions but in singly linked list you can only traverse in one direction with "Next" pointer.
