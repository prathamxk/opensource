# maps are key - value pairs where you can look for the key and get the corresponding value for that key in the map.
# can be compared simliar to co-ordinates on real maps, if we know the co-ordinates(key) we know the name of the place (mostly)

# sets - abstract concept, similar to list, collection of things.
# set doesn't have ordering but doesn't allow duplicates.
# map = < key, value >
# a group of keys is a set ( should not be duplicated ), keys in a map are similar to words in a dictionary and should be unique.
# group of keys in a map without any order is called a set.
# in python maps = dictionaries
"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""


"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""

from collections import OrderedDict

locations = {'North America': {'USA': ['Sunnyvale', 'Mountain View']}, 'Africa': {'Egypt': ['Cairo']}, 'Asia': { 'India' :['Bangalore'], 'China' : ['Shanghai'] }}

# prints only cities in USA in sorted order.
continent = locations.get('North America')
print("1")
for country in continent:
    if country == "USA":
        sortedarray = sorted(continent.values())
        for i in sortedarray:
            print(sorted(i))
          #  print(i)
        #for i in continent:
        #    print(continent[i])

