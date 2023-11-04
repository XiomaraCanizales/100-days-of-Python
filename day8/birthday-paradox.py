""" 
Determinate the probability for people to share the same birthday 
Explore the surprising probabilities of the 'Birthday paradox'
Tags: short, math, simulation
"""
import datetime, random

def getBirthdays(numberofBirthdays):
    """returns a lisr of number random date objects for birthdays """
    birthdays = []

    for i in range(numberofBirthdays):
        # the year is unimportant for the simulation, as long as all birthdays have the same year
        startOfYear = datetime.date(2001, 1, 1)

        # get a random day into the year:
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)

    return birthdays

def getMatch(birthdays):
    """ retuns the date object of a birthday that occurs more than once in the birthdays list """
    if len(birthdays) == len(set(birthdays)):
        # all birthdays are unique
        return None
    
    # compare each birthday to every other birthday
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays):
            if birthdayA == birthdayB:
                # return the matching birthday
                return birthdayA

print('''
      ***Birthday Paradox***
      The Birthday Paradox shows that in a group of N people, the odds that two
      of them have matchin birthdays is surprisingly large.
      This program does a Monte Carlo simulation (that is, repeated random simulations)
      to explore this concept.
      ''')

# set up a tuple of month names in order
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numDays = int(response)
        break

# generate and display birthdays
print('Here are ', numDays, ' birthdays:')
birthdays = getBirthdays(numDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(',', end=' ')
        monthName = MONTHS[birthday.month - 1]
        dateText = '{} {}'.format(monthName, birthday.day)
        print(dateText, end='')

# determinate if there are two birthdays that match
match = getMatch(birthdays)

# display the results
print('In this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print('Multiple people hace a birthday on: ', dateText)
else:
    print('No matching birthdays')

# run through 100,000 simulations
print('Generating ', numDays, 'random birhtdays 100,000 times')
input('Press Enter to begin...')
print('Let\'s run another 100,000 simulations')

# how many simulations had matching birthdays in them
simMatch = 0
for i in range(100_000):
    # report progress every 10,000 simulations
    if i % 10_000 == 0:
        print(i, 'simulations run...')
    birthdays = getBirthdays(numDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('100,000 simulations run')

# display results
probability = round(simMatch / 100_000 * 100, 2)
print('Out of 100,000 simulations of ', numDays, ' people, there was a')
print('matching birthday in that group ', simMatch, ' times. This means')
print('that ', numDays, ' people have a ', probability, '% chance of')
print('having a matching birhtday in their group')
