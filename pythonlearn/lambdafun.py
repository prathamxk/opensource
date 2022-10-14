# normal functions need a function declaration and definition both.
# lambda functions are inline functions defined at same place we use it, so we don't need to declar it somewhere and revisit the code. 
# they are also known as anonymous functions as they don't need to have a name.
a = 1
b = 2
simple_lambda = lambda x,y : x + y
print(simple_lambda(a,b))