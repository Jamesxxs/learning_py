print('')
print('[18.1 Card objects]','-'*70)


class Card:
    """Represents a standard playing card"""
    suit_names = ['clubs','Diamonds','Hearts','Spades']
    rank_names = [None, 'Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

    def __init__(self,suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],Card.suit_names[self.suit])

    def __lt__(self, other):
        t1 = (self.suit,self.rank)
        t2 = (other.suit,other.rank)
        return t1 < t2


queen_of_diamonds = Card(1,12)
print(queen_of_diamonds)


print('')
print('[18.2 Class attributes]','-'*70)
card1 = Card(2,11)
print(card1)

print('')
print('[18.3 Comparing cards]','-'*70)
three_of_clubs = Card(0,3)
print(three_of_clubs)
two_of_diamonds = Card(1,2)
print(two_of_diamonds)

print(two_of_diamonds > three_of_clubs)


print('')
print('[18.4 Decks]','-'*70)
import random

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):#0-3
            for rank in range(1,14):#1-13
                card = Card(suit,rank)
                self.cards.append(card)

    def __str__(self):
        s = []
        for card in self.cards:
            s.append(str(card))
        return '\n'.join(s)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self,other):
        return self.cards.append(other)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self,hand,num):
        for i in range(num):
            hand.add_card(self.pop_card())



print('')
print('[18.5 Printing the deck]','-'*70)
deck1 = Deck()
print(deck1)

print('')
print('[18.6 Add,remove,shuffle and sort]','-'*70)
deck1.shuffle()
print('[shuffled]','-'*30,':\n',deck1)
deck1.sort()
print('[sorted]','-'*30,':\n',deck1)

print('')
print('[18.7 Inheritance]','-'*70)
class Hand(Deck):
    """Represents a hand of playing cards"""
    def __init__(self,label=''):
        self.cards = []
        self.label = label

hand = Hand('new hand')
print(hand.cards)
print(hand.label)

deck = Deck()
#card = deck.pop_card()
#hand.add_card(card)
#print(hand)
deck.move_cards(hand,7)
print(hand)

print('')
print('[18.8 Class diagrams]','-'*70)


print('')
print('[18.9 Debugging]','-'*70)

print('')
print('[18.1 Data encapsulation]','-'*70)
