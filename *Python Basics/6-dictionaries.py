planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)

#A for loop over a dictionary will loop over its keys
numbers = {'one':1, 'two':2, 'three':3}
for k in numbers:
    print("{} = {}".format(k, numbers[k]))

# access a collection of all the keys or all the values 
# with dict.keys() and dict.values()
print(' '.join(sorted(planet_to_initial.values())))
print(' '.join(sorted(planet_to_initial.keys())))

#dict.items() method lets us iterate over the keys and values of a dictionary simultaneously.
for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))

help(str)
