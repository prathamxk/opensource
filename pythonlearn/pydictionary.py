# A dictionary is a data type similar to arrays, but works with keys and values instead of indexes. 
# Each value stored in a dictionary can be accessed using a key, 
# which is any type of object (a string, a number, a list, etc.) instead of using its index to address it.

# example
from itertools import count


phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
#print(phonebook)

# Iterating over dictionaries
# Dictionaries can be iterated over, just like a list. 
# However, a dictionary, unlike a list, does not keep the order of the values stored in it. 
# To iterate over key value pairs, use the following syntax:

phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

# to remove value from dictionary you can use either del or pop functions

phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
del phonebook["John"]
# print(phonebook)
phonebook.pop("Jack")

# dictionaries udacity
locations = {'North America': {'USA': ['Mountain View', 'Sunnyvale', 'Irvine']}, 'Africa': {'Egypt': ['Cairo']}, 'Asia': { 'India' :['Bangalore'], 'China' : ['Shanghai'] }}

continent = locations.get('North America')
for country in continent:
    if country == "USA":
        for i in continent:
            print(sorted(continent[i]))


