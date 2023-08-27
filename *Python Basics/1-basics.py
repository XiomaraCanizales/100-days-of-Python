# *** DATA TYPES ***
dashes = '-------'

# NUMBERS
print(10)
num = 123456789
print(num)
print(dashes)

# BOOLEANS
print(True)
f_bool = False
print(f_bool)
print(dashes)

# STRINGS
print("Harry Potter")
got = 'Game of Thrones'
print(got)
empty = ""
print(empty)
print(dashes)

# NONE KEYWORD
val = None
print(val)
print(type(val))
print(dashes)

# STRING SLICING
my_string = 'This is MY string!'
print(my_string[0:4])
print(my_string[8:len(my_string)])
# slicing with a step
print(my_string[0:7:2])
# reverse slicing
print(my_string[13:2:-1])
# partial slicing
print(my_string[:8])
print(my_string[8:])
print(my_string[:])
print(my_string[::-1])
print(dashes)

# STRING OPERATORS
# concatenation
first = "Bat"
second = "man"
print(first + second)
print("ha" * 3)
# search
random_string = "This is a random string"
print('of' in random_string)
print('random' in random_string)
print(dashes)

numbers = "0123456789"
print(numbers[-2:-6:-2])