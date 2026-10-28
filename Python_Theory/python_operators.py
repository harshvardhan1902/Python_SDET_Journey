"""
Python Operators:
    1. OPerators are used to perform action on variables and values
    2. There are 8 types of operators in python
        -> Arithmetic Operators
        -> Assignment Operators
        -> Ternary Operator
        -> Comparison Operators
        -> Logical Operators
        -> Identity Operators
        -> Membership Operators
        -> Btiwise Operators
"""

"""
Arithmetic Operators:
    1. These are used with numeric values to perform common mathematical operations
    2. There are 7 Arithmetic Operators
        -> Addition = +
        -> Subtraction = -
        -> Multiplication = *
        -> Division = /
        -> Floor Division = //
        -> Modulus = %
        -> Exponentiation = **
"""

a = 10
b = 5

# Example of Addition
print (a + b)

# Example of Subtraction
print (a - b)

# Example of Multiplication
print (a * b)

# Example of Division
print (a / b)

# Example of Floor Division
print (a // b)

# Example of Modulus
print (a % b)

# Example of Exponentiation
print (a ** b)

"""
Assignment Operators:
    1. Assignment Operators are used to assign values to variables
    2. There are total 14 assignment operators that we can use in Python
        -> =
        -> +=
        -> -=
        -> *=
        -> /=
        -> //=
        -> %=
        -> **=
        -> :=
"""

# Example of =
c = 15

# Example of +=
c += c
print (c)

# Example of -=
c -= c
print (c)

# Example of *=
d = 20
d *= d
print (d)

# Example of /=
e = 10
e /= e
print (e)

# Example of //=
d //= d
print (d)

# Example of %=
f = 5
f %= f
print (f)

# Example of **=
g = 2
g **= g
print (g)

# Note := this is also called walrus operator
# it let's us assign a value to a variable and use that value in same expression

# Example without := 
name = "Python"
length = len(name)

if length > 5:
    print(length)

# Example with :=
name = "Python"

if (length := len(name)) > 5:
    print(length)

"""
Ternary Operators:
    1. The ternary operator allows you to assign one value if a condition is true, and another if it is false

Note: The ternary operator is not an actual operator, it is a conditional expression, or a shorthand if statement.
"""

num = 6

x = "WEEKEND!" if num > 5 else "Workday"

print(x)

"""
Comparison Operator:
    1. Comparison Operators are used to compare two values
    2. There are 6 comparison operators
        -> == Equal
        -> != Not Equal
        -> > Greater than
        -> < Less than
        -> >= Greater than or equal to
        -> <= less than or equal to
    3. It gives output as True or False based on comparison
    4. We use logical operators to chain comparison operators together
"""

x = 5
y = 4

# Example of ==
print (x == y)

# Example of !=
print (x != y)

# Example of >
print (x > y)

# Example of <
print (x < y)

# Example of >=
print (x >= y)

# Example of <=
print (x <= y)

"""
Logical Operators:
    1. Logical operators are used to combine conditional statements
    2. They are of three types
        -> and = Returns True if both statements are true
        -> or = Returns True if one of the statements is true
        -> not = Reverse the result, returns False if the result is true
"""

# Example of and

x = 5
y = 6
z = 7
print (x < y and y < z)

# Example of or
print (x > y or y < z)

# Example of not
print (not (x < y and y < z))

"""
Identity Operators:
    1. Identity operators are used to compare the objects
    2. It compare their memory location not their equality
    3. They are of two types
        -> is = Returns True if both variables are the same object
        -> is not = Returns True if both variables are not the same object

Note: Both == and is are different, former compares equality based on values assigned to them while the latter compares their memory location
"""

# Example of is
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)

# Example of is not

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)

# Difference between == and is
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)

x = 5
z = 5
print (x == z)
print (x is z)

# small integers such as 5 are cached and reused. Therefore, both variables typically refer to the same integer object, so the result is True.

"""
Membership Operator:
    1. Membership operators are used to test if a sequence is presented in an object
    2. Results in True or False Output
    3. They are of two types:
        -> in = Returns True if a sequence with the specified value is present in the object
        -> not in = Returns True if a sequence with the specified value is not present in the object
"""

# Example of in
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)

# Example of not in
fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)

# Membership in Strings
text = "Hello World"
print("H" in text)
print("hello" in text)
print("z" not in text)

"""
Operator Precendence:
    1. Operator precedence describes the order in which operations are performed
    2. The Operator precedence in pythona are in following order from highest to lowest
        -> () = Parentheses
        -> ** = Exponentiation
        -> *, /, //, % = Multiplication, division, floor division, and modulus
        -> +, - = Addition and subtraction
        -> ==, !=, >, >=, <, <=, is, is not, in, not in = Comparisons, identity, and membership operators
        -> not = Logical NOT
        -> and = Logical AND
        -> or = Logical OR

    3. If two operators have the same precedence, the expression is evaluated from left to right.
"""