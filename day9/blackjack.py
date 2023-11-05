"""
Blackjack
The Classic card game also known as 21
Tag: large, game, card game
"""

import random, sys

# set up the constants
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'

def main():
    print('''
          ***Blackjack***
          Rules:
          - Try to get as close to 21 without going over
          - Kings, Queens and Jacks are worth 10 points
          - Aces are worth 1 or 11 points
          - Cards 2 through 10 are worth their face value
          - (H)it to take another card
          - (S)tand to stop taking cards
          - On your first play, you can (D)ouble down to increase your bet
          but must hit exactly one more time before standing
          - In case of a tie, the bet is return to the player
          - The Dealer stops hitting at 17.
    ''')

    money = 5000

    # main game loop
    while True:
        # check if player has run out of money
        if money <= 0:
            print('You\'re broke')
            print('Thanks for playing!')
            sys.exit()

        # let player enter theri bet for this round
        print('Money: ', money)
        bet = getBet(money)

        # give the dealer and player two cards from the deck each
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        # handle player actions
        print('Bet: ', bet)
        # keep looping until player stands or bust
        while True:
            displayHands(playerHand, dealerHand, False)
            print()

            # check if the player has bust
            if getHandValue(playerHand) > 21:
                break

            # get the player's move, either H, S, D
            move = getMove(playerHand, money - bet)

            # handle player actions
            if move == 'D':
                # player is doubling down, they can increase their bet
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print('Bet increased to {}'.format(bet))
                print('Bet: ', bet)

            if move in ('H', 'D'):
                #hit/doubling down takes another card
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}'.format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    # the player has busted
                    continue

            if move in ('S', 'D'):
                # stand/doubling down stops the player's turn
                break
        
        # handle dealer's action
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                # dealer hits
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    # the dealer has busted
                    break
                input('Press Enter to continue...')
                print('\n\n')
            
        # show the final hands
        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)

        # handle whether the player won, lost of tied
        if dealerValue > 21:
            print('Dealer busts! You win ${}!'.format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('You lost!')
            money -= bet
        elif playerValue > dealerValue:
            print('You won ${}!'.format(bet))
            money += bet
        elif playerValue == dealerValue:
            print('It\'s a tie, the bet returned to you')
        
        input('Press Enter to continue...')
        print('\n\n')

def getBet(maxBet):
    """Ask the player how much money they want to bet for this round"""
    
    # keep asking until they enter a valid amount
    while True:
        print('How much do you bet? (1-{}, or QUIT)'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing')
            sys.exit()
        
        if not bet.isdecimal():
            # if the player didn't enter a number, ask again
            continue

        bet = int(bet)
        if 1 <= bet <= maxBet:
            # player entered a valid bet
            return bet
        
def getDeck():
    """Return a lis of (rank, suit) tuples for all 52 cards"""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        # add the numbered cards
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        # add the face and ace cards
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck

def displayHands(playerHand, dealerHand, showDealerHand):
    """Show the player's and dealer's cards. Hide de dealers first"""
    print()
    if showDealerHand:
        print('DEALER: ', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ????')
        # hide the dealer's first card
        displayCards([BACKSIDE] + dealerHand[1:])
    
    # show the player cards
    print('PLAYER: ', getHandValue(playerHand))
    displayCards(playerHand)

def getHandValue(cards):
    """Returns the value of the cards. Face cards are worth 10, aces are worth 11 or 1 (this function picks the most suitable ace value)"""
    value = 0
    numberOfAces = 0

    # add the value for the non-ace cards
    for card in cards:
        # card is a tuple (rank, suit)
        rank = card[0]
        if rank == 'A':
            numberOfAces += 1
        # face cards are worth 10 points
        elif rank in ('K', 'Q', 'J'):
            value += 10
        # number cards are worth their number
        else:
            value += int(rank)
        
    # add the value for the aces
    # add 1 per ace
    value += numberOfAces
    for i in range(numberOfAces):
        # if another 10 can be added with busting, do so
        if value + 10 <= 21:
            value += 10
    return value

def displayCards(cards):
    """Display all the cards in the cards list"""
    
    # the text display on each row
    rows = ['', '', '', '', '']

    for i, card in enumerate(cards):
        # print the top line of the card
        rows[0] += ' ___ '
        if card == BACKSIDE:
            # print card's back
            rows[1] += '|##_|'
            rows[2] += '|###|'
            rows[3] += '|_##|'
        else:
            # print the card's front
            # the card is a tuple data structure
            rank, suit = card
            rows[1] += '|{} |'.format(rank.ljust(2))
            rows[2] += '| {} |'.format(suit)
            rows[3] += '|_{}|'.format(rank.rjust(2, '_'))

    # print each row on the screen
    for row in rows:
        print(row)

def getMove(playerHand, money):
    """Asks the player for their move, and returns 'H' for hit, 'S' for stand and 'D' for double down"""
    
    # keep looping until player enters a correct move
    while True:
        # deeterminate what moves the player can make
        moves = ['(H)it', '(S)tand']

        # the player can double down on their first move, which can tell because they'll have exactly two cards
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')

        # get the player's move
        movePromt = ', '.join(moves) + '> '
        move = input(movePromt).upper()
        if move in ('H', 'S'):
            return move
        if move == 'D' and '(D)ouble down' in moves:
            return move

# If the program is run, run the game:
if __name__ == '__main__':
    main()