# Functions are a convenient way to divide your code into useful blocks, 
# allowing us to order our code, make it more readable, reuse it and save some time.
# Also functions are a key way to define interfaces so programmers can share their code.
# A block is a area of code of written in the format of:

# Functions in python are defined using the block keyword "def", followed with the function's name as the block's name.

def my_function():
    print("Hello From My Function!")

# example function with arguments.
def p_function(username, greeting): print("Hello %s how is your %s"%(username, greeting))

# function can return value with keyword return
def sum_two_numbers(a, b):
    return a + b


# simple example of functions working together
def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!"%benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()