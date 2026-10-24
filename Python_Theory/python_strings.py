"""
Strings in Python:

    1. They are surrounded by either single quotes or double qoutes and triple single quotes or triple double quotes.
    2. We can use quotes inside a string, as long as they don't match the quotes surrounding the string
    3. Strings in Python are arrays of unicode characters.
    4. Python does not have a character data type, a single character is simply a string with a length of 1
"""

# approach one of string declaration
string_one = 'Hello World'
print (string_one, type(string_one))

# approach two of string declaration
string_two = "Hello World"
print (string_two, type(string_two))

# approach three of string declaration
string_three = '''Hello World'''
print (string_three, type(string_three))

# approach four of string declaration
string_four = """Hello World"""
print (string_four, type(string_four))

# Approach one Declaring a multi line string
string_multi_one = """A quick
brown fox
jump over
a lazy dog"""
print (string_multi_one)

# Approach two Declaring a multi line string
string_multi_two = '''A quick
brown fox
jump over
a lazy dog'''
print (string_multi_two)

# Example of quotes within Quotes
print ("It's alright")
print ("He is called 'Johnny'")
print ('He is called "Johnny"')

# Example of String as arrays
string_array = "Hello World"
print (string_array[0])
print (string_array[1])
print (string_array[2])
print (string_array[3])
print (string_array[4])
print (string_array[5])
print (string_array[6])
print (string_array[7])
print (string_array[8])
print (string_array[9])
print (string_array[10])

# Looping through a string

for x in "banana":
    print (x)

# Example of len() function
string_length = "Hello I love Python Programming"
print (len(string_length))

# checking in string
string_check = "Hello World"
print ('a' in string_check)

# checking not in string
print ('a' not in string_check)

"""
Slicing through strings
"""