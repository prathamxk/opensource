
astring = "Hello world!" * 5
#find length of string
len(astring)

#find index of letter
astring.index("o")

#count number of specific characters in string
astring.count("l")

#slice operations
# slice string from index 3 till 6 and before 7. Note that index 7 is not counted.
astring[3:7] #same output as next

# slice string from index 3 till 6 for 1 character as a step. Note, even if not mentioned default value of step is 1.
astring[3:7:1] #same output as previous

# slice function to reverse string. Note, when mentioned negative values step starts from the end of the string.
# to reverse a string we should use following function
astring[::-1]

# Note, step cannot be zero for slice function. you can do reverse slice of string as well
astring[:7:-1] # prints !dlr

# make upper case or lower case
print(astring.upper())
print(astring.lower())

# starts with function and ends with function
print(astring.startswith("Hello"))
print(astring.endswith("ld"))

# splits the string into a bunch of strings grouped together in a list based on specific character
print(astring.split(" "))
