
# PYTHON BASIC FROM ZERO.
#
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# COMMENT simple (with hashtag).
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
Multiples 
lineas de 
comentario
con 3 doble comillas
"""

'''
con 3 comillas simples
'''

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# DISPLAY IN CONSOLE:
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

print ('-------------------------------------------------')
print ('Hola Mundo') # NO se necesita punto_y_coma al final!!
print ('-------------------------------------------------')


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# DATA TYPES:
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

print (type(10))                  # Int
print (type(3.14))                # Float
print (type(1 + 3j))              # Complex
print (type('Asabeneh'))          # String
print (type([1, 2, 3]))           # List
print (type({'name':'Asabeneh'})) # Dictionary
print (type({9.8, 3.14, 2.7}))    # Set
print (type((9.8, 3.14, 2.7)))    # Tuple
print ('-------------------------------------------------')


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# VARIABLES IN PYTHON
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

'''
- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)
- Use underscore to use "reserved words" as a variable (see below)
'''

first_name = 'Asabeneh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Asabeneh', 
    'country':'Finland',
    'city':'Helsinki'
    }

# Printing the values stored in the variables
print ('First name:', first_name)
print ('First name length:', len(first_name))
print ('Country: ', country)
print ('City: ', city)
print ('Age: ', age)
print ('Married: ', is_married)
print ('Skills: ', skills)
print ('Person information: ', person_info)
print ('-------------------------------------------------')


# Declaring multiple variables in one line
first_name, last_name, country, age, is_married = 'Clark', 'Hetfield', 'USA', 725, True

print (first_name, last_name, country, age, is_married)
print ('First name:', first_name)
print ('Last name: ', last_name)
print ('Country: ', country)
print ('Age: ', age)
print ('Married: ', is_married)
print ('-------------------------------------------------')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# PYTHON RESERVED WORDS
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

help ('keywords')

'''
False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not         
'''

dir(str) 

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# INPUTS (entries)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# name = input('¿What is your name? ')
# age = input('¿How old are you? ')
# print ("Name:", name, "Age:", age)
print ('-------------------------------------------------')


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ARITHMETIC OPERATIONS
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Integers
print ('Addition: ', 1 + 2)
print ('Subtraction: ', 2 - 1)
print ('Multiplication: ', 2 * 3)
print ('Division: ', 4 / 2)      # Division in python gives floating number
print ('Division without the remainder: ', 7 // 2)   # gives without the floating number or without the remaining
print ('Modulus: ', 3 % 2)        # Gives the remainder
print ('Exponential: ', 3 ** 2)   # it means 3 * 3

# Floating numbers
print ('Floating Number (PI):', 3.1415)
print ('Floating Number (gravity):', 9.81)

# Complex numbers
print ('Complex number: ', 1 + 1j)
print ('Multiplying complex number: ',(1 + 1j) * (1-1j))
print ('-------------------------------------------------')

# Declaring the variable at the top first
a = 3 
b = 2

total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

print (total, diff, product, division, remainder, floor_division, exponential)
print ('-------------------------------------------------')


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# CASTING OPERATIONS (convert between data types)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# int to float
num_int = 10
print ('num_int',num_int)         # 10
num_float = float(num_int)
print ('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print (int(gravity))             # 9

# int to str
num_int = 10
print (num_int)                  # 10
num_str = str(num_int)
print (num_str)                  # '10'

# str to int or float
num_str = '10.6'
#print ('num_int', int(num_str))      # 10 (for some reason returns error)
print ('num_float', float(num_str))  # 10.6

# str to list
first_name = 'Asabeneh'
print (first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print (first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']
print ('-------------------------------------------------')


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# STRINGS
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Concatenate
print ("Hello" + "World")
#print ("Hello " + 5) # Error!!!
print ("Hola " + str(5)) # OK!!
print ("Hola " * 3)  # Print 3 times.

# Multi line
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print (multiline_string)

# Scape sequences
'''
\n: new line
\t: Tab means(8 spaces)
\\: Back slash
\': Single quote (')
\": Double quote (")
'''

print ('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print ('Days\tTopics\tExercises') # adding tab space or 4 spaces 
print ('Day 1\t5\t5')
print ('Day 2\t6\t20')
print ('Day 3\t5\t23')
print ('Day 4\t1\t35')
print ('This is a backslash  symbol (\\)') # To write a backslash
print ('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote
print ('-------------------------------------------------')


# Format strings
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print (formated_string)  # I am Asabeneh Yetayeh. I teach Python
print ('-------------------------------------------------')

a = 4
b = 3
print ('{} + {} = {}'.format(a, b, a + b))   # 4 + 3 = 7
print ('{} - {} = {}'.format(a, b, a - b))
print ('{} * {} = {}'.format(a, b, a * b))
print ('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print ('-------------------------------------------------')

# Strings  and numbers
radius = 12
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print (formated_string)  # The area of a circle with a radius 12 is 452.16.
print ('-------------------------------------------------')


# String interpolation
a = 4
b = 3
print (f'{a} + {b} = {a +b}')      # 4 + 3 = 7
print (f'{a} - {b} = {a - b}')     # 4 - 3 = 1
print (f'{a} * {b} = {a * b}')     # 4 * 3 = 12
print (f'{a} / {b} = {a / b:.2f}') # 4 / 3 = 1.33
print (f'{a} % {b} = {a % b}')     # 4 % 3 = 1
print (f'{a} // {b} = {a // b}')   # 4 // 3 = 1
print (f'{a} ** {b} = {a ** b}')   # 4 ** 3 = 64
print ('-------------------------------------------------')


# Sequences of characters
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print (a) # P
print (b) # y
print (c) # t

# Indexes (start with 0)
print (language[0]) # P
print (language[1]) # y
print (language[2]) # t

last_index = len(language) - 1
print (language[last_index]) # n
print ('-------------------------------------------------')

# Slice strings
language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print (first_three) #Pyt
last_three = language[3:6]
print (last_three) # hon

# Another way
last_three = language[-3:]
print (last_three)   # hon
last_three = language[3:]
print (last_three)   # hon
print ('-------------------------------------------------')

# Reversing strings
greeting = 'Hello, World!'
print (greeting[::-1]) # !dlroW ,olleH
print ('-------------------------------------------------')


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# STRING METHODS
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

language = 'python'
print (language.capitalize()) # Set first character to capital letter
print (language.upper())     # Set string to capital letter
print (language.lower())     # Set string to lower letter
print (language.swapcase())  # Converts all uppercase characters to lowercase and viceversa.
print (language.count("t"))  # Returns occurrences of substring in string.
print (language.isnumeric()) # Checks if all characters in a string are numbers or number related.
print ("1".isnumeric())    # True.
print (language.lower().isupper()) # Checks if ALL alphabet characters in the string are uppercase.
print (language.startswith("Py"))  # Checks if String starts with the Specified String.
print (language.endswith('tion'))  # Checks if String ends with the Specified String.
print (language.split('t'))  # ['py', 'hon'] => Splits the string, using given string or space as a separator.
print (language.replace('y','u'))  # Replaces substring with a given string.
print (language.strip('y'))      # Removes all given characters starting from the beginning and end of the string.

challenge = 'thirty days of pythoonnn'
print (challenge.strip('noth')) # 'irty days of py'

print ("Py" == "py")  # It's not the same.
print ('-------------------------------------------------')


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# LISTS []
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

'''
A list is collection of different data types which is ordered and modifiable (MUTABLE). 
A list can be empty or it may have different data type items.
'''

# Definition (2 ways)
my_list = list() # Built-in function.
my_other_list = [] # square brackets.
print (len(my_list), len(my_other_list)) # 0 0
print (type(my_list))  # class 'list'.


# Access
my_list = [35, 24, 62, 52, 30, 30, 17]
first_element = my_list[0] # 35
last_element = my_list[len(my_list) - 1] # 17
last_element = my_list[-1] # 17
second_last_element = my_list[-2] # 30
#error_element = my_list[100] # wrong index.
print ('-------------------------------------------------')


# Unpacking list items
lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print (first_item)     # item1
print (second_item)    # item2
print (third_item)     # item3
print (rest)           # ['item4', 'item5']
print ('-------------------------------------------------')

first, second, third, *rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print (first)          # 1
print (second)         # 2
print (third)          # 3
print (rest)           # [4,5,6,7,8,9]
print (tenth)          # 10
print ('-------------------------------------------------')


# Slicing items from lists
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4]  # it returns all the fruits
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest.

orange_and_mango = fruits[1:3]  # it does not include the first index.
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2]  # We used a 3rd argument "step". It will take every 2nd item - ['banana', 'mango']

all_fruits = fruits[-4:]   # it returns all the fruits (negative index).
orange_and_mango = fruits[-3:-1] # it does not include the last index, ['orange', 'mango'].
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end, ['orange', 'mango', 'lemon'].
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order, ['lemon', 'mango', 'orange', 'banana'].

print ('-------------------------------------------------')

# checking items
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print (does_exist)  # True

print ('-------------------------------------------------')

# +++++++++++++++++++++++
# MANIPULATE LISTS:
# +++++++++++++++++++++++

fruits = ['banana', 'orange', 'mango', 'lemon']

fruits.append('apple')    # Add to the end -- ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.insert(2, 'apple') # insert 'apple' between 'orange' and 'mango'
fruits.remove('banana')   # ['orange', 'mango', 'lemon']
fruits.pop()              # Remove and return item at index (default last). -- ['banana', 'orange', 'mango']
fruits.pop(1)             # ['banana', 'mango', 'lemon']
fruits.clear()            # [] -- Remove all the elements.
fruits.copy()             # ['banana', 'orange', 'mango', 'lemon']
colors = ['red', 'white', 'blue', 'red', 'green', 'red', 'black']
colors.count('red')       # 3 -- Return number of occurrences of value.
colors.index('blue')      # 2 -- Return first index of value. 'ValueError' if the value is not present.
colors.reverse()          # ['black', 'red', 'green', 'red', 'blue', 'white', 'red']

fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]             # ['orange', 'mango', 'lemon'] -- Remove the item by index.
del fruits                # Remove the list.


# Extend
num1 = [0, 1, 2, 3]
num2= [4, 5,6]
num1.extend(num2)     #  [0, 1, 2, 3, 4, 5, 6]

# sort
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()          # Alphabetical -- ['banana', 'lemon', 'mango', 'orange']
fruits.sort(reverse=True)   # Inverse -- ['orange', 'mango', 'lemon', 'banana']

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()           # Numerical -- [19, 22, 24, 24, 24, 25, 25, 26]
ages.sort(reverse=True)     # Inverse -- [26, 25, 25, 24, 24, 24, 22, 19]
print ('-------------------------------------------------')


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# TUPLES: ()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

'''
A tuple is a collection of different data types which is ordered and unchangeable (IMMUTABLE). 
Tuples are written with round brackets, (). 
Once a tuple is created, we cannot change its values (NO add, insert, remove, because it is immutable).
'''

# Definition (2 ways)

empty_tuple = tuple() # Using the tuple constructor.
empty_tuple = ()  # Empty collection.
fruits = ('banana', 'orange', 'mango', 'lemon')  # With initial values.
tuple1 = ("abc", 34, True, 40, "male")           # With different types.
tuple2 = tuple(("abc", 34, True, 40, "male"))    # It's the same (double parentesis).

print (len(fruits))    # 4
print (type(fruits))   # <class 'tuple'>


# Tuple with ONE element

thistuple = ("apple",)  # ended with comma.
print (type(thistuple))  # <class 'tuple'>

thistuple = ("apple")
print (type(thistuple))  # <class 'str'>


# Access elements

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")

first_element = my_tuple[0]   # 35
last_element = my_tuple[-1]   # "Brais"
last_element = my_tuple[len(my_tuple) - 1]  # "Brais"
second_last_element = my_tuple[-2]          # "Moure"
# my_tuple[4]  => IndexError
# my_tuple[-6] => IndexError


print (my_tuple.count("Brais"))  # 2
print (my_tuple.index("Moure"))  # 3
print (my_tuple.index("Brais"))  # 2 (the first entry)


# Subtuples

print (my_tuple[2:4])    # ('Brais', 'Moure') => Elements 2 and 3.


# Concatenation

even = (2,4,6,8,10)
odd = (1,3,5,7,9)

numbers = even + odd

# Conversions

print (numbers)         #  (2, 4, 6, 8, 10, 1, 3, 5, 7, 9) => Tuple !!
print (sorted(numbers)) #  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] => List !!
#print (numbers.sort())  => AttributeError: 'tuple' object has no attribute 'sort'

sorted_list = sorted(numbers)   # Convert the 'tuple' into a sorted 'list'.
print (type(sorted_list))       # <class 'list'>
print (type(numbers))           # <class 'tuple'>
list_numbers = list(numbers)    # Convert the 'tuple' into a 'list'.
print (type(list_numbers))      # <class 'list'>


# +++++++++++++++++++
# Modify a tuple 
# JUST CONVERT TO LIST AND COVERT BACK TO TUPLE:
# +++++++++++++++++++

vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
# vegetables[0] = 'Letucce' # TypeError: 'tuple' object does not support item assignment

vegetables_tmp = list(vegetables)   # 1) Convert to list.
vegetables_tmp[0] = 'Letucce'       # 2) Add, Modify, Remove ...
vegetables_tmp.insert (1, 'Pea')    # ...
vegetables = tuple(vegetables_tmp)  # 3) Convert back to tuple.

print (vegetables)        #  ('Letucce', 'Pea', 'Potato', 'Cabbage', 'Onion', 'Carrot') => Tuple!!
print (vegetables_tmp)    #  ['Letucce', 'Pea', 'Potato', 'Cabbage', 'Onion', 'Carrot'] => List!!

del (vegetables)        # Remove 'tuple'
del (vegetables_tmp)    # Remove 'list'
print ('-------------------------------------------------')


# Checking items in a tuple

fruits = ('banana', 'orange', 'mango', 'lemon')
print ('orange' in fruits)   # True
print ('apple' in fruits)    # False


# Unpacking tuples

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print (green)    # apple
print (yellow)   # banana
print (red)      # cherry

print ('-------------------------------------------------')


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# SETS: {}
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

'''
In Python set is used to store UNIQUE items, has UNSORTED elements and it is possible to find:
union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.
'''

# Definition
my_set = set()      # using set constructor.
my_other_set = {}   # Empty set ==> It's a dictionary!!

print(type(my_set))         # <class 'set'>
print(type(my_other_set))   # <class 'dict'> ==> Initially, empty set it's a dictionary.


# syntax
st = {'item1', 'item2', 'item3', 'item4'}
fruits = {'banana', 'orange', 'mango', 'lemon'}

# Length
print (len(st))   # 4

# check item
print ('item3' in st)   # True

# Add one item
st.add('item5')
print (st)        # {'item3', 'item4', 'item5', 'item2', 'item1'} => It's NOT sorted.

# Can't have duplicates
st.add('item5')
st.add('item5')
st.add('item5')
print (st)        # {'item4', 'item2', 'item3', 'item5', 'item1'} => UNIQUE values.

# Add multiple elements: 
# ----------------------
# 1) UPDATE(): inserts a set into a given set
st.update(['item6','item7','item8'])  # Update a set with the union of itself and others.
print (st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print (fruits)

# 2) UNION(): Join two sets, returns a new set
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print (fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
print ('-------------------------------------------------')



# Remove items
st.remove('item1')  #  If the item is not found it will raise error.
print (st)

# Remove random item
st.pop()
print (st)

# Which random item is removed?
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop()   # this retuns the removed element.
print (removed_item)
print (fruits)

# Clear set
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print (fruits)        # set()
print (type(fruits))  # <class 'set'>

# Delete set
st = {'item1', 'item2', 'item3', 'item4'}
del st
# print (st)  # NameError: name 'st' is not defined.
print ('-------------------------------------------------')


# Converting 'List' to 'Set'
# Converting list to set removes duplicates and only unique items will be reserved!!

lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered

fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}
print (fruits)
print ('-------------------------------------------------')


# INTERSECTION: returns a set of items which are in both the sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2)    # {'item2', 'item3'}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print (python.intersection(dragon))     # {'o', 'n'}
print ('-------------------------------------------------')

# Check SUBSET and SUPERSET
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False
{'n','o'}.issubset(python)  # True
dragon.issuperset({'r','o','n'})  # True
print ('-------------------------------------------------')

# DIFFERENCE: returns a set of difference between two sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set()
st1.difference(st2) # {'item1', 'item4'} => st1\st2

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'} => Elements that NOT are in 'dragon'
dragon.difference(python)     # {'d', 'r', 'a', 'g'} => Elements that NOT are in 'python'
print ('-------------------------------------------------')

# SYMMETRIC DIFFERENCE: 
#  it returns a set that contains all items from both sets, 
#  except items that are present in both sets, mathematically: (A\B) ∪ (B\A)
#  (lo contrario a "INTERSECTION")
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
print (whole_numbers.symmetric_difference(some_numbers))  # {0, 6, 7, 8, 9, 10}
print (whole_numbers.intersection(some_numbers))          # {1, 2, 3, 4, 5}
print ('-------------------------------------------------')

# DISJOINT SETS:
# If two sets do not have a common item or items we call them disjoint sets.
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print (even_numbers.isdisjoint(odd_numbers)) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print (python.isdisjoint(dragon))  # False, there are common items {'o', 'n'}
print ('-------------------------------------------------')



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# DICTIONARIES: {}
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


my_dict = dict()      # dict constructor
my_other_dict = {}    # curly brackets.

print(type(my_dict))        # <class 'dict'>
print(type(my_other_dict))  # <class 'dict'>

my_other_dict = {"Nombre": "Brais",
                 "Apellido": "Moure", 
                 "Edad": 35, 
                 1: "Python"}

my_dict = {
    "Nombre": "Brais",
    "Apellido": "Moure",
    "Edad": 35,
    "Lenguajes": ["Python", "Swift", "Kotlin"],
    1: 1.77,
    'Address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

print (len(my_dict))    # 5 (count the pairs 'key:value')
print ('-------------------------------------------------')

# ACCESS items
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print (dct['key1'])   # value1
print (dct['key4'])   # value4

print (my_dict['Lenguajes'][0])   # Python
print (my_dict['Address']['zipcode'])   # 02210

# NOTE: Accessing an item by key name raises an error if the key does not exist. 
print ('-------------------------------------------------')

# ADD items to dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'
print (dct)
print ('-------------------------------------------------')

# MODIFY items
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'new_value'
print (dct)
print ('-------------------------------------------------')

# CHECK if key exist
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct)  # True
print('key5' in dct)  # False
print ('-------------------------------------------------')

# REMOVE items
'''
- pop(key): removes the item with the specified key name.
- popitem(): removes the last item.
- del: removes an item with specified key name.
'''

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # removes the last item
del dct['key2'] # removes key2 item
print ('-------------------------------------------------')

# PRINT items (pairs), keys and values in a LIST ():
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
print (dct.items())   # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])
print (dct.keys())    # dict_keys(['key1', 'key2', 'key3'])
print (dct.values())  # dict_values(['value1', 'value2', 'value3'])
print ('-------------------------------------------------')

# CLEAR dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear())    # None
print ('-------------------------------------------------')

# DELETE dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct
print ('-------------------------------------------------')

# COPY a dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
dct_copy = dct.copy()
print (dct_copy)    # {'key1':'value1', 'key2':'value2', 'key3':'value3'}
print ('-------------------------------------------------')



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# CONDITIONALS (if / elif / else )
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

'''
if condition:
  action
'''
a = 3
if a > 0: # Don't forget colon (:).
  print (a, "is a positive number") # Don't forget indention (tab) 

'''
if not condition
  code
'''
my_string = ""
if not my_string:
  print ("Empty string!")

'''
if condition:
  action1
else:
  action2
'''
a = -6
if a < 0:
  print (a, 'is a negative number')
else:
  print (a, 'is a positive number')

'''
if condition1:
  code1
elif condition2:
  code2
else:
  code3
'''
a = 0
if a > 0:
  print (a, 'is a positive number')
elif a < 0:
  print (a, 'is a negative number')
else:
  print (a, 'is zero')

'''
Short hand:
code if condition else code
'''
a = 3
print(a, 'is positive') if a > 0 else print(a, 'is negative') 

'''
if condition1 and condition2:
  code
'''
a = 8
if a > 0 and a % 2 == 0:
  print(a, 'is an even and positive integer')

'''
if condition1 or condition2:
  code
'''
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
  print ('Access granted!')
else:
  print ('Access denied!')
    
print ('-------------------------------------------------')



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# LOOPS ( while / for )
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

'''
while condition:
  code
'''




print ('-------------------------------------------------')
print ('-------------------------------------------------')
print ('-------------------------------------------------')
print ('-------------------------------------------------')
print ('-------------------------------------------------')