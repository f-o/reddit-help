import random


def generate_deck():
    """
    Generates a deck of 52 cards
    """
    deck = []
    for suit in ['Spades', 'Clubs', 'Diamonds', 'Hearts']:
        for value in range(1, 14):
            deck.append((value, suit))
    return deck

def main():
    # Generate deck
    deck = generate_deck()

    # Shuffle deck
    random.shuffle(deck)

    # Pick 5 random cards
    hand = deck[:5]

    # Print hand
    for card in hand:
        print(card)

    # If all cards are the same suit, print FLUSH
    if len(set(card[1] for card in hand)) == 1:
        print('FLUSH')

    # If all cards are consecutive values, print STRAIGHT
    sorted_hand = sorted(card[0] for card in hand)
    if sorted_hand == list(range(sorted_hand[0], sorted_hand[0]+5)):
        print('STRAIGHT')


if __name__ == '__main__':
    main()


