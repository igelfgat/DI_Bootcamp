#Daily Challenge: OOP Quizz
"""Part 1 : Quizz :

Answer the following questions

What is a class?
What is an instance?
What is encapsulation?
What is abstraction?
What is inheritance?
What is multiple inheritance?
What is polymorphism?
What is method resolution order or MRO?


Part 2: Create A Deck Of Cards Class.

The Deck of cards class should NOT inherit from a Card class.

The requirements are as follows:

The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
The Deck class :
should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck."""
import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    
    def __init__(self):
        self.cards = []
        self.create_deck()
        self.shuffle()

    def create_deck(self):
        self.cards = []
        for suit in self.suits:
            for value in self.values:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        self.create_deck()
        random.shuffle(self.cards)

    def deal(self):
        if self.cards:
            return self.cards.pop()
        else:
            return None

# Example usage:
deck = Deck()
print(deck.deal())  # Deals one card
deck.shuffle()      # Shuffles the deck
print(deck.deal())  # Deals another card