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
    1. In Python we use slicing to extract specific part of string.
    2. Syntax = Specify the start index and the end index, separated by a colon, to return a part of the string.
"""

string_slice = "hello World"

# example of string slicing = general slicing
print (string_slice[2:5])

# Slicing string from start = By leaving out starting index, we began from beginning by default
print (string_slice[:5])

# Slicing to the end = By leaving ending index, we slice through end
print (string_slice[2:])

# Negative Slicing
print (string_slice[-5:-2])

# Reversing a string
string_reverse = "Hello Python"
print (string_reverse[::-1])

# We have + operator to concatenate two strings
a = "Hello"
b = "World"
c = a + b
print (c)

# We can also add " " to add spaces between our strings
c = a + " " + b
print (c)

"""
F-strings:
    1. F-String was introduced in Python 3.6
    2. To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
    3. A placeholder can include a modifier to format the value. A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals.
"""

# Example of f-strings
age = 35
print (f"My name is Harsh and I am {age} old")

# Example of modifier f-strings
price = 57
print (f"The price is {price:.2f} dollars")

# Example of math placeholder
price = 25
print (f"The price is {price * 10.75} dollars")

"""
Escape Characters in String:
    1. To insert characters that are illegal in a string, use an escape character.
    2. An escape character is a backslash \ followed by the character you want to insert.

\' or \" = adding single or double quote
\\ = add a single backslash
\n = for new line
\t = for tab
\b = for backspace
\r = for carriage return
\f = for form feed
"""

# \ooo = for octal value
# \xhh = for hexal value

# Example inserting double quotes on a word in string
txt = "We are \'Vikings\'"
print (txt)

# Example of backslash
txt_slash = "We are \\Vikings"
print (txt_slash)

# Example of New Line
txt_new_line = "We are \nVikings"
print (txt_new_line)

# Example of Tab
txt_tab = "We are \tVikings"
print (txt_tab)

# Example of Backspace
txt_backspace = "We are \bVikings"
print (txt_backspace)

"""
String Methods:
    1. These are the built in methods for strings to use in python

length() = to calculate length of string

capitalize() = Converts the first character to upper case

casefold() = Converts string into lower case

center() = Returns a centered string

count() = Returns the number of times a specified value occurs in a string

encode() = 	Returns an encoded version of the string

endswith() = Returns true if string ends with the specified value

find() = Searches the string for a specified value and returns the position of where it was found, if character is not found -1 is returned

format() = Formats specified values in a string

format_map() = Formats specified values in a string

index() = Searches the string for a specified value and returns the position of where it was found, if character not found error message is returned

isalnum() = Returns True if all characters in the string are alphanumeric

isalpha() = Returns True if all characters in the string are in the alphabet

isascii() = Returns True if all characters in the string are ascii characters

isdecimal() = Returns True if all characters in the string are decimals

isdigit() = Returns True if all characters in the string are digits

isidentifier() = Returns True if the string is an identifier

islower() = Returns True if all characters in the string are lower case

isnumeric() = Returns True if all characters in the string are numeric

isprintable() = Returns True if all characters in the string are printable

isspace() = Returns True if all characters in the string are whitespaces

istitle() = Returns True if the string follows the rules of a title

isupper() = Returns True if all characters in the string are upper case

join() = Joins the elements of an iterable to the end of the string

lower() = Converts a string into lower case

partition() = Returns a tuple where the string is parted into three parts

replace() = Returns a string where a specified value is replaced with a specified value

rfind() = Searches the string for a specified value and returns the last position of where it was found, it returns -1 if not found

rindex() = Searches the string for a specified value and returns the last position of where it was found, if not found it gives value error

split() = Splits the string at the specified separator, and returns a list

startswith() = Returns true if the string starts with the specified value

strip() = Returns a trimmed version of the string

swapcase() = Swaps cases, lower case becomes upper case and vice versa

title() = Converts the first character of each word to upper case

upper() = Converts a string into upper case
"""

# Length of String
string_length = "Hello"
print (len(string_length))

# Example of Capitalize
string_capitalize = "hello world"
print (string_capitalize.capitalize())

# Example of caseforld
string_casefold = "HELLO WORLD"
print (string_casefold.casefold())

# Example of center
string_center = "Hello World"
print (string_center.center(100))

# Example of count
string_count = "Hello World"
print (string_count.count('l'))

# Example of encode
string_encode = "Hello World"
print (string_encode.encode())

# Example of endswith
string_endswith = "Hello World"
print (string_endswith.endswith('d'))

# Example of expandtabs
string_expandtabs = "Hello\tWorld"
print (string_expandtabs.expandtabs(10))

# Example of find
string_find = "Hello World"
print (string_find.find('a'))

# Example of format
string_format = "Python"
txt = "Hello {}"
print (txt.format(string_format))

# Example of format_map
text = "Hello {name}"
data = {"name": "Rahul"}
print(text.format_map(data))

# Example of index
string_index = "Hello World"
print (string_index.index('W'))

# Example of alnum
string_isalnum = "Hello1234"
print (string_isalnum.isalnum())

# Example of isalpha
string_isalpha = "Hello World"
print (string_isalpha.isalpha())

# Example of isascii
string_isascii = "Hello@1234"
print (string_isascii.isascii())

# Example of isdecimal
string_isdecimal = "123456"
print (string_isdecimal.isdecimal())

# Example of isdigit
string_isdigit = "Hello123"
print(string_isdigit.isdigit())

# Example of isidentifier
string_isidentifier = "123Hello"
print (string_isidentifier.isidentifier())

# Example of islower
string_islower = "Hello World"
print (string_islower.islower())

# Example of isnumeric
string_isnumeric = "1234565"
print (string_isnumeric.isnumeric())

# Example of isprintable
string_isprintable = ""
print (string_isprintable.isprintable())

# Example of isspace
string_isspace = "Python 12345"
print (string_isspace.isspace())

# Example of istitle
string_istitle = "hello python"
print (string_istitle.istitle())

# Example of isupper
string_isupper = "HELLO PYTHON"
print (string_isupper.isupper())

# Example of join
string_first= "Hello"
string_second = "Python"
print(" ".join([string_first,string_second]))

# Example of lower
string_lower = "HELLOW PYTHON"
print (string_lower.lower())

# Example of partition
string_partition = "Hello to Python"
print(string_partition.partition("to"))

# Example of replace
string_replace = "Hello to Java"
print (string_replace.replace("Java","Python"))

# Example of rfind
string_rfind = "Hello Python"
print (string_rfind.rfind('a'))

# Example of rindex
string_rindex = "Hello Python"
print (string_rindex.rindex("P"))

# Examaple of split
string_split = "Hello Python"
print (string_split.split())

# Example of startswith
string_startswith = "Hello Python"
print (string_startswith.startswith('H'))

# Example of strip
string_strip = " Hello Python "
print (string_strip.strip())

# Example of swapcase
string_swapcase = "Hello Python"
print (string_swapcase.swapcase())

# Example of title
string_title = "hello python"
print (string_title.title())

# Example of upper
string_upper = "hello python"
print (string_upper.upper())