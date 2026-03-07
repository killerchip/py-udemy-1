# Thousands notation
1_000

# Scientific notation
1.2234e12

# Operators
# power **
print ("2 ** 3 =", 2 ** 3)  # 8
# modulo
print ("10 % 3 =", 10 % 3)  # 1
# integer division
print ("10 // 3 =", 10 // 3)  # 3


# Variables

avar = 10
print ("avar =", avar)

# Variables naming
variable123 = 123
# conventional variable naming / snake case
my_variable = "my variable"
_variable = "variable with underscore"

# Strings quotes
my_string = "Hello, World!"
my_variable = 'Python is great!'

# Quotes inside strings
quote_string = "She said, 'Hello!'"
quote_string = 'He said, "Python is awesome!"'

# Triple quotes
multi_line_string = """This is a multi-line string.
It can span multiple lines."""
print (multi_line_string)

# String operators

# concatenation
greeting = "Hello, " + "World!"

# repetition
laugh = "Ha" * 3  # "HaHaHa"

# string indexing
first_char = greeting[0]  # 'H'
last_char = greeting[-1]  # '!'
# string slicing
substring = greeting[0:5]  # 'Hello'
# string length
length = len(greeting)  # 13


# Special value "None"
my_variable = None
print ("my_variable =", my_variable)  # None

# Escape sequences
newline_string = "Hello,\nWorld!"
tabbed_string = "Hello,\tWorld!"
backslash_string = "This is a backslash: \\"
quote_string = "He said, \"Hello!\""
single_quote_string = 'It\'s a beautiful day!'
unicode_string = "Unicode test: \u03A9"  # Omega symbol
print (unicode_string)  # Unicode test: Ω
raw_string = r"C:\Users\Name\Documents" # explanation: raw string ignores escape sequences
print (raw_string)  # C:\Users\Name\Documents

# Type casting
int_to_float = float(10)  # 10.0
float_to_int = int(10.99)  # 10
int_to_str = str(123)  # '123'
str_to_int = int("456")  # 456
str_to_float = float("78.9")  # 78.9
str_to_bool = bool("Hello")  # True
empty_str_to_bool = bool("")  # False
bool_zero = bool(0)  # False
bool_nonzero = bool(42)  # True

# Type checking
print ("Type of int_to_float:", type(int_to_float))  # <class 'float
print ("Type of float_to_int:", type(float_to_int))  # <class 'int'>
print ("Type of int_to_str:", type(int_to_str))  # <class 'str
print ("Type of str_to_int:", type(str_to_int))  # <class 'int'>
print ("Type of str_to_float:", type(str_to_float))  # <class 'float
print ("Type of str_to_bool:", type(str_to_bool))  # <class 'bool
print ("Type of empty_str_to_bool:", type(empty_str_to_bool))  # <class 'bool'>
print ("Type of bool_zero:", type(bool_zero))  # <class 'bool'>
print ("Type of bool_nonzero:", type(bool_nonzero))  # <class 'bool

# F-strings
name = "Alice"
age = 30
greeting = f"My name is {name} and I am {age} years old."
print (greeting)  # My name is Alice and I am 30 years old.

# String methods
upper_string = "hello".upper()  # "HELLO"
lower_string = "WORLD".lower()  # "world"
strip_string = "  hello  ".strip()  # "hello"
strip_chars_string = "xxxyhelloyyy".strip("xy")  # "hello"
replace_string = "hello world".replace("world", "Python")  # "hello Python
split_string = "apple,banana,cherry".split(",")  # ['apple', 'banana', 'cherry']
join_string = "-".join(["2024", "06", "15"])  # "2024-06-15"
find_index = "hello".find("e")  # 1
count_substring = "banana".count("a")  # 3
starts_with = "hello".startswith("he")  # True
ends_with = "hello".endswith("lo")  # True
is_alpha = "hello".isalpha()  # True
is_digit = "12345".isdigit()  # True
capitalize_string = "hello world".capitalize()  # "Hello world": explanation: capitalizes first letter of the string
title_string = "hello world".title()  # "Hello World" explanation: capitalizes first letter of each word
center_string = "hello".center(11, '*')  # "***hello***": explanation: centers the string within a field of given width, padded by specified character
# l-strip and r-strip
lstrip_string = "   hello   ".lstrip()  # "hello   "
rstrip_string = "   hello   ".rstrip()  # "   hello"
# method chaining
chained_string = "   hello world   ".strip().upper().replace("WORLD", "PYTHON")  # "HELLO PYTHON"

# Fasley values
print (bool(""))  # False
print (bool(0))  # False
print (bool(0.0))  # False
print (bool([]))  # False
print (bool(()))  # False
print (bool({}))  # False
print (bool(set()))  # False
print (bool(None))  # False

# in operator
print ("a" in "apple")  # True
print ("b" in "apple")  # False
print (1 in [1, 2, 3])  # True
print (4 in [1, 2, 3])  # False
print ("key" in {"key": "value"})  # True
print ("value" in {"key": "value"})  # False

# If operators and expressions
x = 10
if x > 5:
    print ("x is greater than 5")
else:
    print ("x is not greater than 5")

# else if (elif)
if x > 15:
    print ("x is greater than 15")
elif x > 5:
    print ("x is greater than 5 but not greater than 15")
else:
    print ("x is not greater than 5")

# complex expressions including parentheses
y = 20
if (x > 5 and y > 15) or (x < 5 and y < 15):
    print ("Complex condition is true")
else:
    print ("Complex condition is false")

# Random generators
import random
random_int = random.randint(1, 100)  # Random integer between 1 and
print ("Random integer between 1 and 100:", random_int)
random_float = random.uniform(0.0, 1.0)  # Random float between 0.0 and 1.0
print ("Random float between 0.0 and 1.0:", random_float)
random_choice = random.choice(["apple", "banana", "cherry"])  # Randomly selects one item from the list
print ("Random choice from the list:", random_choice)
random_sample = random.sample([1, 2, 3, 4, 5], 3)  # Randomly selects 3 unique items from the list
print ("Random sample of 3 unique items from the list:", random_sample)

# Loops
# for loop
for i in range(5,2,10):
    print ("For loop iteration:", i)
# iterables
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print ("Iterating over list item:", item)
my_string = "Hello"
for char in my_string:
    print ("Iterating over string character:", char)

# while loop
count = 0
while count < 5:
    print ("While loop count:", count)
    count += 1

# break and continue
for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    if i % 2 == 0:
        continue  # Skip even numbers
    print ("Current value of i:", i)

# FUNCTIONS
def greet(name):
    return f"Hello, {name}!"
print (greet("Alice"))  # Hello, Alice!
def add(a, b):
    return a + b
print (add(5, 3))  # 8

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print (factorial(5))  # 120
# Default parameters
def greet(name="World"):
    return f"Hello, {name}!"
print (greet())  # Hello, World!
# order of default parameters
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
print (greet("Alice"))  # Hello, Alice!
print (greet("Alice", "Hi"))  # Hi, Alice!
# keyword arguments
print (greet(greeting="Hi", name="Bob"))  # Hi, Bob!
# Lambda functions
square = lambda x: x ** 2 # explanation: lambda functions are anonymous functions defined using the lambda keyword, they can take any number of arguments but can only have one expression
print (square(5))  # 25

# Complex lamda function with multiple optional arguments and complex body
complex_lambda = lambda x, y=10: (x ** 2 + y ** 2) ** 0.5  # explanation: this lambda function calculates the distance from the origin to the point (x, y) in a 2D space, with y having a default value of 10
print (complex_lambda(3))  # 10.44...
print (complex_lambda(3, 4))  # 5.0

# SCOPES: LEGB = Local, Enclosing, Global, Built-in
# Global: variables defined at the top level of a script or module
# Local: variables defined within a function
# Enclosing: variables defined in the local scope of any and all enclosing functions
# Built-in: names preassigned in the built-in names module
# Scope prcendence: Local > Enclosing > Global > Built-in

# Global keyword: used to declare that a variable inside a function is global (i.e., it should not be treated as a local variable)
# Global keyword example:
counter = 0  # Global variable
def increment():
    global counter  # Declare that we are using the global variable 'counter'
    counter += 1  # Increment the global variable
increment()
print ("Counter after incrementing:", counter)  # Counter after incrementing: 1

# LISTS

# Creating a list
my_list = [1, 2, 3, 4, 5]
print ("My list:", my_list)  # My list: [1, 2, 3, 4, 5]

# list keyword
my_list = list([1, 2, 3, 4, 5])
print ("My list using list keyword:", my_list)  # My list using list keyword:

# List indexing
first_item = my_list[0]  # 1
last_item = my_list[-1]  # 5
print ("First item:", first_item)  # First item: 1
print ("Last item:", last_item)  # Last item: 5

# List length
list_length = len(my_list)  # 5

# List methods 
my_list.append(6)  # [1, 2, 3, 4, 5, 6]
my_list.insert(0, 0)  # [0, 1, 2, 3, 4, 5, 6]
my_list.remove(3)
print ("List after modifications:", my_list)  # List after modifications: [0, 1, 2, 4, 5, 6]
my_list.extend([7, 8, 9])  # [0, 1, 2, 4, 5, 6, 7, 8, 9]

# List slicing
sublist = my_list[2:5]  # [2, 4, 5]
print ("Sublist from index 2 to 4:", sublist)  # Sublist from index 2 to 4: [2, 4, 5]
reverse_list = my_list[::-1]  # [9, 8, 7, 6, 5, 4, 2, 1, 0]: explanation: this slice reverses the list by using a step of -1
# List[start:stop:step]

# List deletion methods
del my_list[0]  # Deletes the first item (0)
print ("List after deletion:", my_list)  # List after deletion: [1, 2, 4, 5, 6, 7, 8, 9
my_list.pop()  # Removes and returns the last item (9)
print ("List after popping the last item:", my_list)  # List after popping the last
my_list.pop(2)  # Removes and returns the item at index 2 (4)
print ("List after popping item at index 2:", my_list)  # List after popping
