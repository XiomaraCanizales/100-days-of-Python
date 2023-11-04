"""
Deductive logic game.
User must guest a secret three digit number.
User has 10 tries to guess the secret number
Tags: short, game, puzzle
"""

import random

NUM_DIGITS = 3
MAX_GUESSES = 5

def main():
    print('''Bagels, a deductive logic game.
          By Al Sweigart
          I am thinking of a {}-digit number with no repeated digits.
          Try to guess what the number is. Here are some clues:
          When      I say: That means:
            Pico    One digit is correct but in the wrong position
            Fermi   One digit is correct and in the right position
            Bagels  No digit is correct
          '''.format(NUM_DIGITS))
    
    # main game loop
    while True:
        # this stores the secret number the player needs to guess:
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # keep looping until enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}:'.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                # user is correct
                break
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses')
                print('The answer was: {}'.format(secretNum))

        # ask player if wants to play again:
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')
        
def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits"""
    # creates a list of digits 0 to 9
    numbers = list('0123456789')
    # shuffle list inot random order
    random.shuffle(numbers)
    # get the first NUM_DIGITS digits in the list of the secret number
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    """ Returns a string with the pico, fermin, bagels clues for a guess a111nd secret number pair"""
    if guess == secretNum:
        return 'You got it!'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # a correct digit in the correct place
            clues.append('Fermi ')
        elif guess[i] in secretNum:
            clues.append('Pico ')
    # there are no correct digits at all
    if len(clues) == 0:
        return 'Bagels'
    #else:
        # sort the clues in alphabetical order so their original order doesn't give information away
        #clues.sort()
        # make a single string from the list of string clues
    return ''.join(clues)

# If the program is run, run the game:
if __name__ == '__main__':
    main()