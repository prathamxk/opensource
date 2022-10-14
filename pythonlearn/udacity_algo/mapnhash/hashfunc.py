# Hash functions - allows to do lookups in constant time.
# for list, set you need to do lookup in linear time
# How hash functions work ?
# Give it some value to a HASH function it converts the value based on some forumula and gives out a coded value
# example barcode tickets, we need to do fast lookup of ticket numbers.
# common pattern in creating hash functions is to take last 2/3 numbers of a actual value and divide that with a constant number
# put the reminder of that division to find an index or a key where we can store the original value.
# why do this strategy works ? If numbers are big and random, we need to find the way to numbers to convert them into indices quikcly
# why use last 2 digits of numbr/? most of the lists start with number  starting form 1,2,3 so the variation is less,
# if numbers are of higher order like 7,8,9 the variation is more.

# Hash collisions: There are times when hash function can end up giving same values for two different numbers, this is termed as hash collision.
# 2 ways to deal with collision:
# 1. Change the value in your hash function - (the dividing number) - 
# 2. Change the hash function completely - Collection / Bucket
# change the structure of an array, instead of storing 1 value at the index, you can store some type of list which can be called bucket at same index.
# where we can store some type of lists that ocntains all values hashed at that spot.
# if we use option 1 - and store bigger hash value in that case, you are doing to require a lot more space to store your values.
# if we keep on changing the value based on the collision, then the complexity of the algo is going to increase in terms of size and time.
# if we use option 2 bucket - we still need to iterate through some collection, though shorter one. hash functions have constant time in avg case but
# due to bucket system, you end up searching linearly.
# considering above things we need to make hash function which makes the most sense of your data and limitations
# use one large bucket and use small hash buckets inside big bucket.

# Load factor = Number of entries / number of buckets
