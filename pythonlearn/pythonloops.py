
# ------- for loop --------------
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

# range - in python 3 range and xrange work same. in python 2 range returns the specified range
# xrange - xrange returns an iterator which is more efficient
# it is similar to range(start, stop, step)

# ---------- Prints out 3,5,7 ---
for x in range(3, 8, 2):
    print(x)

# -------------- while loops -----
# Prints out 0,1,2,3,4

count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1

# ------------ break ----------
# Prints out 0,1,2,3,4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# --------- continue ----------
# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

# ------ we can use else clause for while / for loop condition failure. If break statement in the loop then else is skipped.
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

