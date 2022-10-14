#---------------- comparison ops !=, ==, <, >, <=, >=

x =2

print(x == 2)

print (x ==3)

print(x < 3)

#---------------- boolean ops AND, OR

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")


#------------- in oprator --- check if value available in list.

name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

#------------ if elif else: statement

x = 2
if x == 2:
    print("x equals two!")
elif x == 3:
    print("x equals three!")
else:
    print("x does not equal to two.")

# statment is evaluated as true if one of hte following is correct:
# 1. The "True" boolean variable is given or calcuated using an expression such as arithmatic comparison
# 2. An object which is not considered "Empty" is passed.

# ------- is operator -------------- Unlike the == op, is doesn't match the values of the variables but instances themselves. TBD
x = [1,2,3]
y = [1,2,3]
print(x ==y)
print(x is y)

# -------- not operator ---- invert the boolean expression
print(not False) # prints True


