"""
Python is a high level popular programming language known for its simple and readable syntax developed by Guido van Rossum and released in 1961.

It is used for :-
    1. Web Developement
    2. Software Developement
    3. Artificial Intelligence
    4. Data Analytics etc.

Why Python?
    1. Python is an open source and dynamically typed programming language
    2. Has automatic garbage collection
    3. It can be treated in a Procedural way, an object oriented way or a functional way

Note :- We will be learning on Python version 3.15.1
"""

"""
This is a multi-line comment
"""

# this is a single line comment

# this is also
# a multi-line comment

"""
Intendation in Python :

    1. Intendation plays a very important role in python
    2. It simply means adding space in front of your line of code.
    3. In python, indentation specifies which line of code belong together
"""

# Example of Correct Indentation

age = 20

if age >=19:
    print ("You are an adult")

print ("The program ran successfully")

# Example of incorrent indentation = expected an indented block after 'if' statement on line 45

# age = 20

# if age >=19:
# print ("You are an adult")

# print ("The program ran successfully")

"""
Variables in Python :-
    1. Used to store data values
    2. Python has no command of declaring a variable
    3. A variable is declared the moment you assign a value to it
    4. Variables do not need to be declared with any particular type, and can even change type after they have been set.
    5. If you want to specify the data type of a variable, this can be done with casting.

type() = This method is used to know the data type of a variable
input() = This method is used to take user inputs within your code in python
print() = This method is used to print end-result of your code in python
id() = This method is used to show an objects identity


Note 1 : String can be written in both single quotes and double quotes
Note 2 : Variable Names are case-sensitive, meaning var = 1, Var = 2, VAR = 3 are different variables with different values assigned to them

Rules for naming a variable in python :
    1. A variable name must start with a letter or the underscore character
    2. A variable name cannot start with a number
    3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    4. Variable names are case-sensitive (age, Age and AGE are three different variables)
    5. A variable name cannot be any of the Python keywords.

Example of some valid variables names :
    1. myvar
    2. my_var
    3. _myvar
    4. myVar
    5. MyVar

Example of some invalid variable names :
    1. 2myvar
    2. my-var
    3. my var


Techniques used to name variables :
    1. Camel Case = Each world except the first starts with a capital letter
        -> Example = myVariableName

    2. Pascal Case = Each word starts with a capital letter
        -> Example = MyVariableName

    3. Sname Case = Each word is separated by an underscore character
        -> Example = my_variable_name
"""

# assigning and printing a value to variable

x = 10
print (x)

# declaring two variables and print them

x = 10
y = 15
print (x, y)

# Assigning Many Values to Many Variabels

x,y,z = 1,2,3
print (x, y, z)

# assigning one value to multiple variables

a = b = c = "Harsh"
print (a, b, c)

# Unpacking a collection

fruits = ["Mango", "Apple", "Banana"]
q , w, e = fruits
print (q, w, e)

"""
User Input:
    1. we use input() function to take user inputs
    2. By default the input will be in string but you can convert it to other forms
"""
# default input

x = input ("Enter your value: ")
print (x)

# taking integer as input

q = int (input ("Enter you age: "))
print (q)

# taking float as input

price = float (input("Enter the price: "))
print (price)

# approach 1 of taking multiple inputs in one line

x, y = input ("Enter the two numbers: ").split()
print (x, y)

# approach 2 of taking multiple inputs

a, b = map (str, input ("Enter the two strings: ").split())
print (a, b)

# taking list as input

a = list (map (int, input("Enter a list of numbers: ").split()))
print (a)

# taking a tuple as input

b = tuple (map(int, input("Enter a tuple of numbers: ").split()))
print (b)

# taking a set as input

c = set (map(int, input("Enter a set of numbers: ").split()))
print (c)

# taking a frozenset as input

d = frozenset(map(int, input("Enter numbers: ").split()))
print(a)