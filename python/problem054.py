# -*- coding: utf-8 -*-
"""
Project Euler Problem 54

http://projecteuler.net/index.php?section=problems&id=54

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

    * High Card: Highest value card.
    * One Pair: Two cards of the same value.
    * Two Pairs: Two different pairs.
    * Three of a Kind: Three cards of the same value.
    * Straight: All cards are consecutive values.
    * Flush: All cards of the same suit.
    * Full House: Three of a kind and a pair.
    * Four of a Kind: Four cards of the same value.
    * Straight Flush: All cards are consecutive values of same suit.
    * Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the
highest value wins; for example, a pair of eights beats a pair of
fives (see example 1 below). But if two ranks tie, for example, both
players have a pair of queens, then highest cards in each hand are
compared (see example 4 below); if the highest cards tie then the next
highest cards are compared, and so on.

Consider the following five hands dealt to two players:
Hand   Player 1            Player 2            Winner
1      5H 5C 6S 7S KD      2C 3S 8S 8D TD      Player 2
       Pair of Fives       Pair of Eights

2      5D 8C 9S JS AC      2C 5C 7D 8S QH      Player 1
       Highest card Ace    Highest card Queen

3      2D 9C AS AH AC      3D 6D 7D TD QD      Player 2
       Three Aces          Flush with Diamonds

4      4D 6S 9H QH QC      3D 6D 7H QD QS
       Pair of Queens      Pair of Queens      Player 1
       Highest card Nine   Highest card Seven

5      2H 2D 4C 4D 4S      3C 3D 3S 9S 9D      Player 1
       Full House          Full House
       With Three Fours    with Three Threes

The file, poker.txt, contains one-thousand random hands dealt to two
players. Each line of the file contains ten cards (separated by a
single space): the first five are Player 1's cards and the last five
are Player 2's cards. You can assume that all hands are valid (no
invalid characters or repeated cards), each player's hand is in no
specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""
from collections import defaultdict

class Card(object):
    """
    Represents a card e.g the Jack of diamonds
    """
    short = "" # set on init
    suits = {'C': "clubs",
             'D': "diamonds",
             'H': "hearts",
             'S': "spades",
             }
    
    values = {2: "two",
              3: "three",
              4: "four",
              5: "five",
              6: "six",
              7: "seven",
              8: "eight",
              9: "nine",
              10: "ten",
              11: "jack",
              12: "queen",
              13: "king",
              14: "ace",
              }

    def __init__(self, card_as_string):
        """

        Initialise with a string e.g. "TS"
        
        First character is a number from 2 - 9 or a letter to represent
        Ten, Jack Queen, King or Ace

        Second character is a letter to represent Clubs, Diamonds,
        Hearts or Spades.
        """
        self.short = card_as_string
        v,s = card_as_string
        try:
            self.value = int(v)
        except ValueError:
            self.value = dict(T=10,
                              J=11,
                              Q=12,
                              K=13,
                              A=14,
                              ).get(v)
        self.suit = s.upper()

    def __unicode__(self):
        return u"%s of %s" % (self.values[self.value], self.suits[self.suit])

    __str__ = __unicode__

    # Comparison operators

    def __lt__(self, other):
        return self.value < other.value

    def __lte__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __gte__(self, other):
        return self.value >= other.value

class Hand(object):
    def __init__(self, cards):
        self.cards = cards
        self.cards.sort(reverse=True)
        self.values_dict = defaultdict(int)
        for c in self.cards:
            self.values_dict[c.value] += 1

    def __str__(self):
        return ",".join(c.short for c in self.cards)

    def is_straight_flush(self):
        if self.is_flush():
            return self.is_straight()
        else:
            return 0

    def is_four_of_a_kind(self):
        if 4 in self.values_dict.values():
            four_of_a_kind, high_card = 0, 0
            for k,v in self.values_dict.values():
                if v==4:
                    four_of_a_kind = k
                else:
                    high_card = k
            return (four_of_a_kind, high_card)
        else:
            return 0

    def is_full_house(self):
        if sorted(self.values_dict.values()) == [2, 3]:
            three_of_a_kind, pair = 0,0
            for k,v in self.values_dict.items():
                if v==3:
                    three_of_a_kind = k
                else:
                    pair_card = k
            return (three_of_a_kind, pair_card)
        else:
            return 0
        
    def is_flush(self):
        suits = set([c.suit for c in self.cards])
        if len(suits) == 1:
            return self.cards[0].value
        else:
            return 0

    def is_straight(self):
        last_card = self.cards[0]
        for card in self.cards[1:]:
            if last_card.value == card.value + 1:
                last_card = card
            else:
                return 0
        return self.cards[0].value

    def is_three_of_a_kind(self):
        if 3 in self.values_dict.values():
            three_of_a_kind, high_card = 0,0
            for k,v in self.values_dict.items():
                if v==3:
                    three_of_a_kind = k
                else:
                    high_card = max(k, high_card)

            return (three_of_a_kind, high_card)
        else:
            return 0

    def is_two_pairs(self):
        if sorted(self.values_dict.values()) == [1,2,2]:
            pair1, pair2, high_card = 0,0,0
            for k,v in self.values_dict.items():
                if v==2:
                    if k > pair1:
                        pair2 = pair1
                        pair1 = k
                    else:
                        pair2 = k
                else:
                    high_card = k
            return (pair1, pair2, high_card)
        else:
            return 0

    def is_one_pair(self):
        if sorted(self.values_dict.values()) == [1,1,1,2]:
            pair = []
            high_cards = []
            for k,v in self.values_dict.items():
                if v==2:
                    pair.append(k)
                else:
                    high_cards.append(k)
            return pair + sorted(high_cards, reverse=True)
        else:
            return 0

    def is_high_card(self):
        return [c.value for c in self.cards]
        

class Player(object):
    hand = None
    def __init__(self):
        self.hands_won = 0

class Game(object):
    deck = ()

    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()

    def get_deck(self):
        self.deck = Deck()

    def play_hand(self, cards):
        self.player1.hand = Hand(cards[:5])
        self.player2.hand = Hand(cards[5:])

        winner = None
        for rank in "straight_flush", "four_of_a_kind", "full_house", "flush", "straight", "three_of_a_kind", "two_pairs", "one_pair", "high_card":
            p1 = getattr(self.player1.hand, "is_%s" % rank)()
            p2 = getattr(self.player2.hand, "is_%s" % rank)()
            
            if p1 and p2:
                if p1 > p2:
                    winner = self.player1
                else:
                    winner = self.player2
            elif p1 and not p2:
                winner = self.player1
            elif p2 and not p1:
                winner = self.player2
            if winner is not None:
                break
                
        winner.hands_won += 1

    def play(self):
        self.get_deck()
        for cards in self.deck:
            self.play_hand(cards)

class Deck(object):
    """
    Holds a deck of cards
    """
    def __init__(self):
        """
        Reads the hands from poker.txt
        """
        f = open('poker.txt', 'r')
        self.hands = f.readlines()
        f.close()

    def __iter__(self):
        for hand_as_string in self.hands:
            yield [Card(card_as_string) for card_as_string in hand_as_string.split()]


def solution():
    """
    """
    game = Game()
    game.play()

    return game.player1.hands_won

if __name__ == "__main__":
    print solution()
