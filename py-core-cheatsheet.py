# =============================================================================
# PYTHON CORE ELEMENTS CHEATSHEET
# =============================================================================

# =============================================================================
# 1. VARIABLES & ASSIGNMENT
# =============================================================================

x = 10                      # integer assignment
name = "Alice"              # string assignment
pi = 3.14                   # float assignment
is_active = True            # boolean assignment

# Multiple assignment
a, b, c = 1, 2, 3
x = y = z = 0              # same value to multiple variables

# Swap variables
a, b = b, a

# Augmented assignment
x += 5                     # x = x + 5
x -= 2                     # x = x - 2
x *= 3                     # x = x * 3
x /= 4                     # x = x / 4
x //= 2                    # x = x // 2 (floor division)
x **= 2                    # x = x ** 2 (exponentiation)
x %= 3                     # x = x % 3 (modulo)

# Constants (convention only, Python has no true constants)
MAX_SIZE = 100
PI = 3.14159

# Deleting a variable
del x

# =============================================================================
# 2. DATA TYPES
# =============================================================================

# --- Numeric Types ---
i = 42                      # int
f = 3.14                    # float
c = 3 + 4j                  # complex
big = 10_000_000            # underscores for readability

# --- Boolean ---
t = True                    # bool (subclass of int: True == 1, False == 0)
f = False

# --- String ---
s1 = 'single quotes'
s2 = "double quotes"
s3 = """triple quotes
for multiline strings"""
s4 = r"raw string: no \n escape"  # raw string

# --- None ---
nothing = None              # represents absence of value

# --- Type checking ---
type(42)                    # <class 'int'>
isinstance(42, int)         # True
isinstance(42, (int, float))  # True (check multiple types)

# --- Type conversion (casting) ---
int("42")                   # str -> int: 42
int(3.9)                    # float -> int: 3 (truncates, no rounding)
float("3.14")               # str -> float: 3.14
str(42)                     # int -> str: "42"
bool(0)                     # int -> bool: False
bool("")                    # str -> bool: False
bool(1)                     # int -> bool: True
bool("hello")              # str -> bool: True
list("abc")                 # str -> list: ['a', 'b', 'c']
tuple([1, 2, 3])            # list -> tuple: (1, 2, 3)
set([1, 2, 2, 3])           # list -> set: {1, 2, 3}

# Falsy values: False, None, 0, 0.0, "", [], (), {}, set()
# Everything else is truthy

# =============================================================================
# 3. STRINGS
# =============================================================================

s = "Hello, World!"

# --- Indexing & Slicing ---
s[0]                        # 'H' (first character)
s[-1]                       # '!' (last character)
s[0:5]                      # 'Hello' (start:stop, stop excluded)
s[7:]                       # 'World!' (from index 7 to end)
s[:5]                       # 'Hello' (from start to index 5)
s[::2]                      # 'Hlo ol!' (every 2nd character)
s[::-1]                     # '!dlroW ,olleH' (reversed)

# --- Common Methods ---
s.lower()                   # 'hello, world!'
s.upper()                   # 'HELLO, WORLD!'
s.strip()                   # remove leading/trailing whitespace
s.lstrip()                  # remove leading whitespace
s.rstrip()                  # remove trailing whitespace
s.split(", ")               # ['Hello', 'World!']
", ".join(["a", "b", "c"])  # 'a, b, c'
s.replace("World", "Python")  # 'Hello, Python!'
s.find("World")             # 7 (index, or -1 if not found)
s.index("World")            # 7 (index, raises ValueError if not found)
s.count("l")                # 3
s.startswith("Hello")       # True
s.endswith("!")              # True
s.isdigit()                 # False
s.isalpha()                 # False
s.isalnum()                 # False
s.title()                   # 'Hello, World!'
s.capitalize()              # 'Hello, world!'
s.center(20, "-")           # '---Hello, World!----'
s.zfill(20)                 # '0000000Hello, World!'

# --- String Formatting ---
name = "Alice"
age = 30

# f-strings (Python 3.6+) - preferred
f"Name: {name}, Age: {age}"
f"Next year: {age + 1}"
f"Pi: {3.14159:.2f}"       # 'Pi: 3.14' (2 decimal places)
f"{'hello':>20}"            # right-align in 20 chars. Explain: 'hello' is right-aligned within a field of 20 characters, padded with spaces on the left.
f"{'hello':<20}"            # left-align in 20 chars. Explain: 'hello' is left-aligned within a field of 20 characters, padded with spaces on the right.
f"{'hello':^20}"            # center in 20 chars. Explain: 'hello' is centered within a field of 20 characters, padded with spaces on both sides.
f"{1000000:,}"              # '1,000,000' (thousands separator)

# .format() method
"Name: {}, Age: {}".format(name, age)   # 'Name: Alice, Age: 30'
"Name: {0}, Age: {1}".format(name, age) # 'Name: Alice, Age: 30' (positional)
"Name: {n}, Age: {a}".format(n=name, a=age) # 'Name: Alice, Age: 30' (keyword)

# % operator (old style)
"Name: %s, Age: %d" % (name, age)   # 'Name: Alice, Age: 30' (%s for string, %d for integer)

# --- String Operations ---
"Hello" + " " + "World"    # concatenation: 'Hello World'
"Ha" * 3                    # repetition: 'HaHaHa'
"ell" in "Hello"            # membership: True
len("Hello")                # length: 5

# =============================================================================
# 4. NUMBERS & MATH
# =============================================================================

# --- Arithmetic Operators ---
10 + 3                      # 13 (addition)
10 - 3                      # 7 (subtraction)
10 * 3                      # 30 (multiplication)
10 / 3                      # 3.3333... (true division, always float)
10 // 3                     # 3 (floor division, integer result)
10 % 3                      # 1 (modulo/remainder)
10 ** 3                     # 1000 (exponentiation)
-10                         # negation

# --- Built-in Math Functions ---
abs(-5)                     # 5
round(3.7)                  # 4
round(3.14159, 2)           # 3.14
pow(2, 10)                  # 1024 (same as 2 ** 10)
pow(2, 10, 1000)            # 24 (2**10 % 1000, modular exponentiation)
min(1, 2, 3)                # 1
max(1, 2, 3)                # 3 args: any number of arguments, returns min/max
sum([1, 2, 3])              # 6 args: iterable of numbers, returns sum
divmod(10, 3)               # (3, 1) -> (quotient, remainder)

# --- math module (import math) ---
# math.sqrt(16)             # 4.0
# math.floor(3.7)           # 3
# math.ceil(3.2)            # 4
# math.pi                   # 3.141592653589793
# math.e                    # 2.718281828459045
# math.log(100, 10)         # 2.0
# math.log2(8)              # 3.0

# =============================================================================
# 5. COMPARISON & LOGICAL OPERATORS
# =============================================================================

# --- Comparison ---
5 == 5                      # True (equal)
5 != 3                      # True (not equal)
5 > 3                       # True (greater than)
5 < 10                      # True (less than)
5 >= 5                      # True (greater than or equal)
5 <= 10                     # True (less than or equal)

# Chained comparisons
1 < 5 < 10                  # True (same as 1 < 5 and 5 < 10)

# --- Logical ---
True and False              # False
True or False               # True
not True                    # False

# Short-circuit evaluation
# `and` returns first falsy value or last value
0 and "hello"               # 0
"hello" and "world"         # "world"

# `or` returns first truthy value or last value
0 or "hello"                # "hello"
"" or "default"             # "default"

# --- Identity ---
x is None                   # True if x is None (identity check)
x is not None               # True if x is not None

# --- Membership ---
"a" in "abc"                # True
1 in [1, 2, 3]              # True
"key" in {"key": "val"}     # True (checks keys in dict)

# =============================================================================
# 6. LISTS
# =============================================================================

lst = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, 3.14, None]  # can hold mixed types
nested = [[1, 2], [3, 4]]
empty = []

# --- Indexing & Slicing (same as strings) ---
lst[0]                      # 1
lst[-1]                     # 5
lst[1:3]                    # [2, 3]
lst[::-1]                   # [5, 4, 3, 2, 1]

# --- Modifying ---
lst[0] = 99                 # replace element
lst[1:3] = [20, 30]         # replace slice

# --- Methods ---
lst.append(6)               # add to end: [1, 2, 3, 4, 5, 6] #args: single element
lst.insert(0, 0)            # insert at index: [0, 1, 2, 3, 4, 5]
lst.extend([7, 8])          # add multiple: [1, 2, 3, 4, 5, 7, 8]
lst.remove(3)               # remove first occurrence of value 3
lst.pop()                   # remove & return last item
lst.pop(0)                  # remove & return item at index
lst.clear()                 # remove all items
lst.index(3)                # index of first occurrence (raises ValueError if missing)
lst.count(3)                # count occurrences
lst.sort()                  # sort in place (ascending)
lst.sort(reverse=True)      # sort in place (descending)
lst.sort(key=len)           # sort by custom key # (e.g., length of elements)
lst.reverse()               # reverse in place
lst2 = lst.copy()           # shallow copy

# --- List Operations ---
[1, 2] + [3, 4]            # [1, 2, 3, 4] (concatenation)
[0] * 5                     # [0, 0, 0, 0, 0] (repetition)
len(lst)                    # length
3 in lst                    # membership check

# --- Built-in functions with lists ---
sorted([3, 1, 2])           # [1, 2, 3] (returns new list)
sorted([3, 1, 2], reverse=True)  # [3, 2, 1]
reversed(lst)               # returns iterator
list(reversed([1, 2, 3]))   # [3, 2, 1]
enumerate(lst)              # returns iterator of (index, value) pairs
zip([1, 2], ["a", "b"])     # returns iterator of (1,'a'), (2,'b')

# --- List Comprehensions ---
squares = [x**2 for x in range(10)] # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
evens = [x for x in range(20) if x % 2 == 0] # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
matrix = [[i * j for j in range(3)] for i in range(3)]
flat = [x for row in matrix for x in row]  # flatten

# [ternary_expression or mapper for item in iterable if filter_condition]
#  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#  transforms every                         drops items before
#  item that passes                         transformation

# --- Unpacking ---
first, *rest = [1, 2, 3, 4]          # first=1, rest=[2, 3, 4]
first, *middle, last = [1, 2, 3, 4]  # first=1, middle=[2, 3], last=4

# =============================================================================
# 7. TUPLES
# =============================================================================

t = (1, 2, 3)
single = (1,)               # single element tuple (comma required!)
empty_t = ()
t2 = tuple([1, 2, 3])       # from list

# Tuples are IMMUTABLE (cannot be modified after creation)
t[0]                        # 1 (indexing works)
t[0:2]                      # (1, 2) (slicing works)
# t[0] = 99                 # TypeError! Cannot modify

t.count(1)                  # 1
t.index(2)                  # 1

# Tuple unpacking
a, b, c = (1, 2, 3)
x, y = (10, 20)             # commonly used

# Tuples as dictionary keys (lists cannot be)
d = {(0, 0): "origin", (1, 0): "right"}

# =============================================================================
# 8. DICTIONARIES
# =============================================================================

d = {"name": "Alice", "age": 30, "city": "NYC"}
empty_d = {}
d2 = dict(name="Alice", age=30)  # alternative creation

# --- Access ---
d["name"]                   # "Alice" (raises KeyError if missing)
d.get("name")               # "Alice" (returns None if missing)
d.get("phone", "N/A")       # "N/A" (custom default)

# --- Modify ---
d["age"] = 31               # update value
d["email"] = "a@b.com"      # add new key-value pair
del d["city"]               # delete key-value pair

# --- Methods ---
d.keys()                    # dict_keys(['name', 'age', 'city'])
d.values()                  # dict_values(['Alice', 30, 'NYC'])
d.items()                   # dict_items([('name','Alice'), ('age',30), ...])
d.pop("age")                # remove & return value for key
d.pop("missing", None)      # remove with default (no error)
d.popitem()                 # remove & return last inserted (key, value)
d.update({"age": 31, "x": 1})  # merge/update from another dict
d.setdefault("key", [])     # get value or set default if missing
d.clear()                   # remove all items
d2 = d.copy()               # shallow copy

# --- Dictionary Comprehensions ---
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

filtered = {k: v for k, v in d.items() if v > 10}

# TERNARIES
numbers = [-2, -1, 1, 2, 3]

# Ternary on the VALUE
{x: "even" if x % 2 == 0 else "odd" for x in numbers if x > 0}
# {1: 'odd', 2: 'even', 3: 'odd'}

# Ternary on the KEY
{("even" if x % 2 == 0 else "odd"): x for x in numbers if x > 0}
# note: keys would overwrite each other here — just illustrating syntax

# --- Merging (Python 3.9+) ---
merged = {"a": 1} | {"b": 2}   # {'a': 1, 'b': 2}

# --- Iterating ---
for key in d:               # iterate over keys
    pass
for key, value in d.items():  # iterate over key-value pairs
    pass

# =============================================================================
# 9. SETS
# =============================================================================

s = {1, 2, 3, 4, 5}
empty_s = set()              # NOT {} (that's an empty dict)
s2 = set([1, 2, 2, 3])      # {1, 2, 3} (removes duplicates)

# Sets are UNORDERED, contain only UNIQUE, HASHABLE elements

# --- Methods ---
s.add(6)                    # add element
s.remove(3)                 # remove (raises KeyError if missing)
s.discard(3)                # remove (no error if missing)
s.pop()                     # remove & return arbitrary element
s.clear()                   # remove all

# --- Set Operations ---
a = {1, 2, 3}
b = {3, 4, 5}

a | b                       # union: {1, 2, 3, 4, 5}
a & b                       # intersection: {3}
a - b                       # difference: {1, 2}
a ^ b                       # symmetric difference: {1, 2, 4, 5}
a.issubset(b)               # False
a.issuperset(b)             # False
a.isdisjoint(b)             # False (they share element 3)

# --- Set Comprehensions ---
evens = {x for x in range(10) if x % 2 == 0}

# --- Frozen Sets (immutable sets) ---
fs = frozenset([1, 2, 3])   # can be used as dict keys or set elements

# =============================================================================
# 10. CONDITIONALS (if / elif / else)
# =============================================================================

x = 10

if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative")

# Ternary (conditional expression)
result = "even" if x % 2 == 0 else "odd"

# Match statement (Python 3.10+)
status = 404
match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown")

# =============================================================================
# 11. LOOPS
# =============================================================================

# --- for loop ---
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2):   # 2, 4, 6, 8 (start, stop, step)
    print(i)

for char in "hello":        # iterate over string characters
    print(char)

for item in [1, 2, 3]:      # iterate over list
    print(item)

for i, val in enumerate(["a", "b", "c"]):  # with index
    print(i, val)

for k, v in {"a": 1}.items():  # iterate dict
    print(k, v)

# --- while loop ---
count = 0
while count < 5:
    print(count)
    count += 1

# --- Loop Control ---
for i in range(10):
    if i == 3:
        continue            # skip rest of this iteration
    if i == 7:
        break               # exit loop entirely
    print(i)

# --- else clause on loops (runs if loop completes without break) ---
for i in range(5):
    if i == 10:
        break
else:
    print("Loop completed without break")

# --- Useful iteration tools ---
# zip: iterate multiple sequences in parallel
for a, b in zip([1, 2, 3], ["x", "y", "z"]):
    print(a, b)             # 1 x, 2 y, 3 z

# enumerate: get index + value
for idx, val in enumerate(["a", "b", "c"], start=1):
    print(idx, val)         # 1 a, 2 b, 3 c

# =============================================================================
# 12. FUNCTIONS
# =============================================================================

# --- Basic function ---
def greet(name):
    """Docstring: explains what the function does."""
    return f"Hello, {name}!"

# --- Default parameters ---
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# --- *args (variable positional arguments) ---
def add_all(*args):
    return sum(args)

add_all(1, 2, 3)            # 6

# --- **kwargs (variable keyword arguments) ---
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30)

# --- Mixed parameters (order matters) ---
def func(pos, /, pos_or_kw, *, kw_only):
    pass
# pos:        positional-only (before /)
# pos_or_kw:  positional or keyword
# kw_only:    keyword-only (after *)

# --- Return multiple values (returns a tuple) ---
def min_max(lst):
    return min(lst), max(lst)

lo, hi = min_max([3, 1, 4, 1, 5])

# --- Lambda (anonymous functions) ---
square = lambda x: x ** 2
square(5)                   # 25

add = lambda a, b: a + b
add(3, 4)                   # 7

# Used with higher-order functions
sorted(["banana", "apple"], key=lambda s: len(s))
list(map(lambda x: x * 2, [1, 2, 3]))      # [2, 4, 6]
list(filter(lambda x: x > 2, [1, 2, 3, 4]))  # [3, 4]

# --- Type hints (annotations, not enforced) ---
def add(a: int, b: int) -> int:
    return a + b

# --- Nested functions & closures ---
def outer():
    x = 10
    def inner():
        return x        # inner can access outer's variables
    return inner

# --- Decorators ---
def my_decorator(func):
    @wraps(func)    # preserves wrapped func metadata
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

# --- Decorators with arguments ---
@my_decorator
def say_hello():
    print("Hello!")

def repeat(n):                 # outer: receives decorator argument
    def decorator(func):       # middle: receives the function
        @wraps(func)
        def wrapper(*args, **kwargs):  # inner: the actual wrapper
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")

say_hi()
# Hi!
# Hi!
# Hi!

# =============================================================================
# 13. SCOPE & NAMESPACES
# =============================================================================

# LEGB Rule: Local -> Enclosing -> Global -> Built-in

x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)        # "local"
    inner()

# global keyword: modify global variable from inside a function
count = 0
def increment():
    global count
    count += 1

# nonlocal keyword: modify enclosing (not global) variable
def outer():
    x = 0
    def inner():
        nonlocal x
        x += 1
    inner()
    return x             # 1

# =============================================================================
# 14. COMPREHENSIONS (summary)
# =============================================================================

# List comprehension
[x**2 for x in range(5)]                    # [0, 1, 4, 9, 16]
[x for x in range(10) if x % 2 == 0]        # [0, 2, 4, 6, 8]

# Dictionary comprehension
{x: x**2 for x in range(5)}                 # {0:0, 1:1, 2:4, 3:9, 4:16}

# Set comprehension
{x % 3 for x in range(10)}                  # {0, 1, 2}

# Generator expression (lazy, memory efficient)
gen = (x**2 for x in range(5))              # generator object
list(gen)                                    # [0, 1, 4, 9, 16]
sum(x**2 for x in range(5))                 # 30

# =============================================================================
# 15. EXCEPTION HANDLING
# =============================================================================

# --- try / except / else / finally ---
try:                                    # code that might raise an exception goes here
    result = 10 / 0                     # this raises ZeroDivisionError
except ZeroDivisionError:              # catches ONLY ZeroDivisionError
    print("Cannot divide by zero")
except (TypeError, ValueError) as e:   # catches EITHER TypeError or ValueError
    print(f"Error: {e}")               # `e` holds the exception message
except Exception as e:                 # catches ANY other exception (catch-all)
    print(f"Unexpected error: {e}")    # put this last, it's the most broad
else:
    print("No exception occurred")     # runs ONLY if try block succeeded (no exception)
finally:
    print("Always runs")               # ALWAYS runs, even if exception was raised
                                        # use for cleanup: closing files, DB connections, etc.

# Execution flow:
# exception raised   -> try -> except -> finally
# no exception       -> try -> else   -> finally

# --- Raising exceptions ---
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

# --- Custom exceptions ---
class CustomError(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code

# raise CustomError("Something went wrong", 500)

# =============================================================================
# 16. CLASSES & OOP
# =============================================================================

class Dog:
    # Class variable (shared by all instances)
    species = "Canis familiaris"

    # Constructor
    def __init__(self, name, age):
        self.name = name        # instance variable
        self.age = age

    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"

    # String representation
    def __repr__(self):
        return f"Dog('{self.name}', {self.age})"

    def __str__(self):
        return f"{self.name}, age {self.age}"

    # Comparison
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    # Class method
    @classmethod
    def from_string(cls, dog_str):
        name, age = dog_str.split(",")
        return cls(name, int(age))

    # Static method
    @staticmethod
    def is_valid_age(age):
        return age > 0

# --- Inheritance ---
class Puppy(Dog):
    def __init__(self, name, age, toy):
        super().__init__(name, age)
        self.toy = toy

    def play(self):
        return f"{self.name} plays with {self.toy}"

# --- Properties ---
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

# --- Dataclasses (Python 3.7+) ---
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2) ** 0.5

# Automatically generates __init__, __repr__, __eq__

# =============================================================================
# 17. FILE I/O
# =============================================================================

# --- Reading ---
with open("file.txt", "r") as f:
    content = f.read()          # read entire file as string

with open("file.txt", "r") as f:
    lines = f.readlines()       # read all lines as list

with open("file.txt", "r") as f:
    for line in f:              # read line by line (memory efficient)
        print(line.strip())

# --- Writing ---
with open("file.txt", "w") as f:   # write (overwrites)
    f.write("Hello\n")

with open("file.txt", "a") as f:   # append
    f.write("More text\n")

# --- Modes ---
# 'r'  read (default)
# 'w'  write (truncates)
# 'a'  append
# 'x'  create (fails if exists)
# 'b'  binary mode (e.g. 'rb', 'wb')
# '+'  read and write (e.g. 'r+')

# =============================================================================
# 18. MODULES & IMPORTS
# =============================================================================

import math                     # import entire module
from math import sqrt, pi       # import specific items
from math import sqrt as square_root  # import with alias
import math as m                # module alias

# Common standard library modules:
# os        - operating system interface
# sys       - system-specific parameters
# json      - JSON encoding/decoding
# re        - regular expressions
# datetime  - date and time
# random    - random number generation
# pathlib   - object-oriented filesystem paths
# collections - specialized container types
# itertools - iterator building blocks
# functools - higher-order functions

# =============================================================================
# 19. USEFUL BUILT-IN FUNCTIONS
# =============================================================================

# --- I/O ---
print("hello", end=" ")    # print without newline
print("a", "b", sep=", ")  # custom separator
input("Enter: ")            # read user input (returns string)

# --- Type & Conversion ---
type(42)                    # <class 'int'>
isinstance(42, int)         # True
int(), float(), str(), bool(), list(), tuple(), set(), dict()

# --- Iterables ---
len([1, 2, 3])              # 3
range(5)                    # 0, 1, 2, 3, 4
range(1, 10, 2)             # 1, 3, 5, 7, 9
enumerate(iterable)         # (index, value) pairs
zip(iter1, iter2)           # parallel iteration
sorted(iterable)            # returns new sorted list
reversed(iterable)          # returns reversed iterator
map(func, iterable)         # apply func to each element
filter(func, iterable)      # keep elements where func returns True
any([False, True, False])   # True (any element is truthy)
all([True, True, False])    # False (not all elements are truthy)
min(1, 2, 3)                # 1
max(1, 2, 3)                # 3
sum([1, 2, 3])              # 6

# --- Other ---
id(obj)                     # unique identifier (memory address)
hash(obj)                   # hash value
dir(obj)                    # list of attributes/methods
help(obj)                   # interactive help
callable(obj)               # True if obj can be called
repr(obj)                   # developer string representation
vars(obj)                   # __dict__ of object

# =============================================================================
# 20. COMMON PATTERNS
# =============================================================================

# --- Ternary expression ---
x = "yes" if condition else "no"

# --- Walrus operator (Python 3.8+) ---
# Assign and use in one expression
if (n := len("hello")) > 3:
    print(f"Length {n} is > 3")

# --- Unpacking with * ---
first, *rest = [1, 2, 3, 4]
head, *_, tail = [1, 2, 3, 4, 5]

# --- Dictionary unpacking ---
defaults = {"color": "red", "size": 10}
custom = {**defaults, "size": 20}  # {'color': 'red', 'size': 20}

# --- Main guard ---
if __name__ == "__main__":
    print("This runs only when script is executed directly")

# --- Assert (for debugging, removed with -O flag) ---
assert 2 + 2 == 4, "Math is broken"

# --- with statement (context managers) ---
with open("file.txt") as f:
    data = f.read()
# File is automatically closed after the block

# =============================================================================
# 21. GENERATORS
# =============================================================================

# Generators produce values one at a time using `yield` instead of `return`
# They are memory-efficient: only one value is held in memory at a time

# --- Basic generator function ---
def count_up(n):
    for i in range(n):
        yield i             # pauses here, gives value, resumes on next call

gen = count_up(3)
next(gen)                   # 0
next(gen)                   # 1
next(gen)                   # 2
# next(gen)                 # StopIteration (exhausted)

# --- Typical usage: just loop over it ---
for val in count_up(5):
    print(val)              # 0, 1, 2, 3, 4

# --- Generator expression (lazy list comprehension) ---
squares_list = [x**2 for x in range(5)]    # list: builds everything now
squares_gen  = (x**2 for x in range(5))    # generator: computes on demand

list(squares_gen)           # [0, 1, 4, 9, 16] (forces full evaluation)
sum(x**2 for x in range(5)) # 30 (no intermediate list needed)

# --- Generators are EXHAUSTED after one pass ---
gen = (x**2 for x in range(5))
list(gen)                   # [0, 1, 4, 9, 16]
list(gen)                   # [] (already exhausted, cannot reuse)

# --- yield from: delegate to another iterable ---
def chain(*iterables):
    for it in iterables:
        yield from it       # yields each item from it one by one

list(chain([1, 2], [3, 4], [5]))  # [1, 2, 3, 4, 5]

# --- Infinite sequences (impossible with lists) ---
def integers_from(n):
    while True:
        yield n
        n += 1

gen = integers_from(0)
next(gen)                   # 0
next(gen)                   # 1 (runs forever, only computes when asked)

# --- Practical example: reading a large file ---
def read_large_file(path):
    with open(path) as f:
        for line in f:
            yield line.strip()  # one line at a time, not the whole file

# for line in read_large_file("huge.txt"):
#     process(line)

# --- List vs Generator comparison ---
# list:      [x**2 for x in range(n)]   -> all n items in memory at once
# generator: (x**2 for x in range(n))   -> one item in memory at a time

# =============================================================================
# PYTHON MODULES, IMPORTS, PACKAGES, VENV & UV CHEATSHEET
# =============================================================================

# =============================================================================
# 21. MODULES & IMPORTS
# =============================================================================

# A module is simply a .py file. Importing it makes its contents available.

# --- Four import styles ---
import math                         # 1. import whole module (safest, no collisions)
math.sqrt(16)                       # access via dot notation: 4.0

from math import sqrt               # 2. import specific name (convenient)
sqrt(16)                            # use directly, no prefix needed

from math import sqrt as sq         # 3. import with alias
sq(16)                              # 4.0

import numpy as np                  # 4. module alias (community convention)
np.array([1, 2, 3])                 # np, pd, plt are widely used aliases

# --- Importing multiple names ---
from math import sqrt, pi, floor    # comma-separated

# --- Wildcard import (avoid in production) ---
from math import *                  # imports everything — can cause name collisions

# --- Common standard library modules ---
import os           # operating system interface (paths, env vars, processes)
import sys          # interpreter internals (sys.argv, sys.path, sys.exit)
import json         # JSON encoding/decoding
import re           # regular expressions
import datetime     # date and time handling
import random       # random number generation
import pathlib      # object-oriented filesystem paths (preferred over os.path)
import collections  # specialized containers: defaultdict, Counter, deque
import itertools    # iterator building blocks: chain, product, combinations
import functools    # higher-order functions: reduce, lru_cache, partial

# =============================================================================
# 22. PACKAGES
# =============================================================================

# A package is a folder containing an __init__.py file.
# It lets you organize related modules together.

# --- Typical structure ---
# my_project/
# ├── main.py
# └── utils/
#     ├── __init__.py        <- marks folder as a package (can be empty)
#     ├── tools.py
#     └── math_helpers.py

# --- Importing from a package ---
from utils.tools import greet           # import specific function
from utils import math_helpers          # import whole module from package
import utils.tools                      # import with full path

# --- __init__.py as a "front door" ---
# utils/__init__.py can expose selected names for cleaner imports:
#
#   from .tools import greet
#   from .math_helpers import add
#
# Then in main.py:
from utils import greet, add            # clean, no need to know internal structure

# --- Relative imports (used inside packages) ---
from .tools import greet                # same package (one dot = current folder)
from ..other import something           # parent package (two dots = one level up)

# --- Nested packages ---
# services/
# ├── __init__.py
# ├── auth/
# │   ├── __init__.py
# │   └── login.py
# └── data/
#     ├── __init__.py
#     └── parser.py

from services.auth.login import authenticate
from services.data.parser import parse_csv

# --- Absolute vs relative (best practice) ---
# Prefer absolute imports for clarity, use relative inside packages
from utils.tools import greet           # absolute — always clear, always works
from .tools import greet                # relative — only works inside a package

# =============================================================================
# 23. VIRTUAL ENVIRONMENTS (venv)
# =============================================================================

# A virtual environment is an isolated Python environment with its own
# site-packages folder. Prevents dependency conflicts between projects.

# --- Creating and activating ---
# python -m venv venv              # create a venv in a folder named "venv"
# source venv/bin/activate         # activate (Mac/Linux)
# venv\Scripts\activate            # activate (Windows)
# deactivate                       # exit the virtual environment

# --- Installing packages inside venv ---
# pip install requests             # installs only into this project's venv
# pip install requests==2.28.0     # specific version
# pip uninstall requests           # remove package
# pip list                         # list installed packages
# pip show requests                # details about a package

# --- Sharing dependencies ---
# pip freeze > requirements.txt    # save exact versions to file
# pip install -r requirements.txt  # recreate environment from file

# requirements.txt looks like:
# requests==2.31.0
# numpy==1.24.0
# pandas==2.0.1

# --- Project structure conventions ---
# my_project/
# ├── venv/               <- NEVER commit to git (add to .gitignore)
# ├── main.py
# ├── utils/
# └── requirements.txt    <- DO commit to git

# =============================================================================
# 24. UV — MODERN PACKAGE MANAGER
# =============================================================================

# uv is a fast, all-in-one Python package manager written in Rust.
# Replaces: pip, venv, pyenv, poetry — 10-100x faster than pip.
# Developed by Astral (creators of Ruff). Released February 2024.

# --- Installation ---
# Mac/Linux:  curl -LsSf https://astral.sh/uv/install.sh | sh
# Windows:    powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
# Via pip:    pip install uv

# --- Starting a new project ---
# uv init my_project               # scaffold a full project
# cd my_project
#
# Creates:
# my_project/
# ├── .venv/                <- virtual env, created automatically
# ├── pyproject.toml        <- replaces requirements.txt
# ├── uv.lock               <- lockfile (exact versions, auto-generated)
# └── main.py

# --- Managing packages ---
# uv add requests                  # install a package
# uv add requests==2.28.0          # specific version
# uv add "requests>=2.28,<3.0"     # version range
# uv remove requests               # uninstall
# uv sync                          # install all deps from lockfile

# --- Running code (no need to activate venv!) ---
# uv run main.py                   # runs with the project's venv automatically
# uv run pytest                    # run any tool in the project env

# --- Python version management ---
# uv python install 3.12           # install a Python version
# uv python install 3.12 3.13      # install multiple versions
# uv python pin 3.12               # pin this project to Python 3.12
# uv run --python 3.11 main.py     # run with a specific version

# --- pip-compatible interface (easy migration) ---
# uv pip install requests          # same as pip install
# uv pip install -r requirements.txt
# uv pip uninstall requests
# uv pip list
# uv pip freeze

# --- pyproject.toml (managed automatically by uv add/remove) ---
# [project]
# name = "my_project"
# version = "0.1.0"
# requires-python = ">=3.12"
# dependencies = [
#     "requests>=2.28.0",
#     "numpy>=1.24.0",
# ]

# =============================================================================
# QUICK REFERENCE: pip + venv  vs  uv
# =============================================================================

# Task                   pip + venv                        uv
# ---------------------  --------------------------------  --------------------
# Create environment     python -m venv venv               automatic
# Activate               source venv/bin/activate          not needed
# Install package        pip install requests              uv add requests
# Uninstall              pip uninstall requests            uv remove requests
# Run script             python main.py                    uv run main.py
# Save dependencies      pip freeze > requirements.txt     automatic (uv.lock)
# Restore dependencies   pip install -r requirements.txt   uv sync
# Install Python ver.    (use pyenv separately)            uv python install 3.12
# Pin Python ver.        (use pyenv separately)            uv python pin 3.12
# Use a list when:   you need to iterate multiple times, index, or get len()
# Use a generator when: the sequence is large, infinite, or used only once
