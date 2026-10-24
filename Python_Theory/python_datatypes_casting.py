"""
Datatypes in Python:
    1. They tell us what type of value we are working with
    2. Common Categories of Datatypes in Python are:
        -> Numeric = int, float, complex
        -> Sequesnce = list, tuple, range
        -> Mapping = dict
        -> Set = set, frozenset
        -> Boolean = bool
        -> None = None
        -> Byte = bytes, bytearray, memoryview
"""

# Example of int
a = 5
print (a, type(a))

# example of float
b = 5.5
print (b, type(b))

# example of complex
c = 5 + 5j
print (c, type(c))

# example of list
d = [1,2,3,4,5]
print (d, type(d))

# example of tuple
e = (1,2,3,4,5)
print (e, type(e))

# example of range
f = range(5)
print (f,type(f))

# example of set
g = {1,2,3,4,5,5}
print (g, type(g))

# example of frozenset
h = frozenset({1,2,3,4,5,5})
print (h, type(h))

# example of bool
i = True
print (i, type(i))

# example of None
j = None
print (j, type(j))

# example of bytes
k = b"1234"
print (k, type(k))

# example of bytearray
l = bytearray(5)
print (l, type(l))

# example of memoryview
m = memoryview(bytes(5))
print (m, type(m))

# to generate a random number in a range we use random() function

import random
x = random.randrange(1,20)
print (x)

"""
Casting in Python:
    1. It means converting value from one data type to another

int = int(), float(), bool(), str(), complex()
float = int(), float(), bool(), str(), complex()
str = str(), list(), tuple(), set(), forzenset()
bool = int(), float(), bool(), str(), complex()

"""

# example of casting

x = 25
y = str (x)
print (y, type(y))

# Implicit Casting in Python

x = 5
y = 7.5
z = x + y
print (z, type(z))

# Explicit casting in Python

x = 5
y = float (x)
z = str (x)
a = complex(x)

print (y, type(y))
print (z, type(z))
print (a, type(a))