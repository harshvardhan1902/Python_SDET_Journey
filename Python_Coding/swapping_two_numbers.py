"""
Code to swap two variables without using a third variable
"""

# Approach 1
a = 10
b = 15

print ("Before Swapping: ", a, b)

a,b = b,a

print ("Afer Swapping: ", a,b)

# Approach 2

x = 25
y = 30

print ("Befor Swapping: ", x, y)

x = x + y
y = x - y
x = x - y

print ("After Swapping :", x, y)