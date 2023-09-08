dashes = '-------'
# function definition
def minimum(first, second):
    if (first < second):
        print(first)
    else: 
        print(second)

minimum(10, 20)
print(dashes)

# return
def maximum(first, second):
    if (first > second):
        return first
    return second

result = maximum(100, 75)
print(result)
print(dashes)

# built-in functions
print('search:')
random_string = 'This is a string'
print(random_string.find('is'))

print('replace:')
a_string = "Welcome home!"
new_string = a_string.replace('Welcome', 'Greetings from')
print(new_string)

print('letter case:')
print('uppercase'.upper())
print('LOWERCASE'.lower())

print('join:')
list = ['a', 'b', 'c']
print('>>'.join(list))

print('formatting:')
string = 'Learn Python {version} at {cname}'.format(version = 3, cname='Educative')
print(string)
print(dashes)

print('lambdas:')
triple = lambda num : num * 3
print(triple(10))

my_func = lambda num: "High" if num > 50 else "Low"
print(my_func(60))
print(dashes)

print('recursion:')
def rec_count(number):
    print(number)
    # base case
    if number == 0:
        return 0
    rec_count(number - 1)
    print(number)
rec_count(5)