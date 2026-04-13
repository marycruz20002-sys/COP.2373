import random

class Card:
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', 
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}'

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def pop_card(self):
        return self.cards.pop()

def deal_hand(deck):
    """Deals 5 cards from the deck into a list."""
    return [deck.pop_card() for _ in range(5)]

def replace_cards(hand, deck):
    """Prompts user to select cards for replacement and draws new ones."""
    print("\nYour current hand:")
    for i, card in enumerate(hand):
        print(f"{i+1}: {card}")

    indices_str = input("\nEnter the numbers of the cards you want to replace (e.g., 1, 3, 5) or 'none': ")
    
    if indices_str.lower() != 'none':
        # Convert input string to a list of integers (adjusting to 0-indexed)
        indices = [int(n.strip()) - 1 for n in indices_str.split(',') if n.strip().isdigit()]
        
        for idx in sorted(indices, reverse=True):
            if 0 <= idx < 5:
                hand.pop(idx)
                hand.insert(idx, deck.pop_card())
    
    return hand

# Main Game Program
if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    
    player_hand = deal_hand(deck)
    player_hand = replace_cards(player_hand, deck)
    
    print("\nYour final hand after the draw:")
    for card in player_hand:
        print(card)
