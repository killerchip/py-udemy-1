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
