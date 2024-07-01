#Daily Challenge: OOP Quizz
"""Part 1 : Quizz :

Answer the following questions

What is a class?
    A class is a blueprint for creating objects (a particular data structure). 
    It defines a set of attributes and methods that the created objects will have.
What is an instance?
    An instance is an individual object created using a class.
What is encapsulation?
    Encapsulation is the concept of bundling the data (attributes) and the methods (functions) that operate on the data into a single unit or class. 
    It also involves restricting direct access to some of an object's components, which can prevent the accidental modification of data.
What is abstraction?
Abstraction is the concept of hiding the complex implementation details of a system and exposing only the necessary and relevant parts
What is inheritance?
Inheritance is a mechanism by which one class (the child) can inherit the properties and methods of another class (the parent).
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

deck = Deck()
print(deck.deal())
deck.shuffle()
print(deck.deal())  