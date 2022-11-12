# Classes are an encapsulation of variables and functions into a single entity.
# Classes are essentially a template to create your objects.
# Objects get their variables and functions from classes.


class FunClass:
    variable = "blah"

    def inst_fun(self):
        print("This is a message inside the class.")

# create object of a class
funclassx = FunClass()
funclassy = FunClass()

# access instance variable through object
print(funclassx.variable)
funclassy.variable = "yvar"
print(funclassy.variable)

# access function using the instance object
funclassx.inst_fun()

# The __init__() function, is a special function that is called when the class is being initiated.
# It's used for assigning values in a class.

class NumberHolder:

   def __init__(self, number):
       self.number = number

# sample exercise
# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here

car1 = Vehicle()
car1.name = "Fer"
car1.kind = "Convertible"
car1.color = "red"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.kind = "van"
car2.color = "red"
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())