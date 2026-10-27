"""
Boolean in Python:
    1. It represents two values True or False
    2. Most Values are true:
        -> Any String is true, except for empty strings
        -> Any number is true, except for zero
        -> Any list, tuple, set, and dictionary are True, except empty ones

    3. Some Values are false:
        -> there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None.
        -> the value False evaluates to False

Note: Function can also return boolean values of True or False
Note: isinstance() function is used to determine if an object is of a certain data type
"""

# Eexample of true values
print (bool("abc"))
print (bool(123))
print (bool(["apple", "cherry", "banana"]))

# Example of false values
print (bool(False))
print (bool(None))
print (bool(0))
print (bool(""))
print (bool(()))
print (bool([]))
print (bool({}))

# Example of isinstance
x = 200
print(isinstance(x, int))