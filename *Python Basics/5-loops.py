# example 1
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ')
print('')

# example 2
multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult
print(product)

# example 3
string = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# print all the uppercase letter in string, one at a time
for char in string:
    if char.isupper():
        print(char, end='')
print('') 

# example 4 - range()
for i in range(5):
    print(i)

# example 5 - while
i = 0
while i < 10:
    print(i, end=' ')
    i += 1

# list comprehensions
# example 6 
squares = [n**2 for n in range(10)]
print(squares)

# example 7 - adding an if condition
short_planets = [planet for planet in planets if len(planet) < 6]
print(short_planets)

# example 8 - if condition and applying some transformation
loud_short_planets = [
    planet.upper() + '!' 
    for planet in planets 
    if len(planet) < 6
    ]
print(loud_short_planets)

# example 9 - simplifing functions
def count_negatives(nums):
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative = n_negative + 1
    return n_negative
print(count_negatives([5, -1, -2, 0, 3]))

# >>> better
def count_negatives_2(nums):
    return len([num for num in nums if num < 0])
print(count_negatives_2([5, -1, -2, 0, 3]))

# >>> even better
def count_negatives_3(nums):
    return sum([num < 0 for num in nums])
print(count_negatives_3([5, -1, -2, 0, 3]))