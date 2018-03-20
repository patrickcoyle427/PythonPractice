#!usr/bin/python3

# cardanddeckclass.py - practice for learning how classes work.
# 
# You can create individual instances of cards, or use the deck class to create a deck to be used in card games.

import random

class Card(object):
  
  possible_suits = ('Club', 'Diamond', 'Heart', 'Spade')    
    
  possible_values = ('2', '3', '4', '5', '6', '7', '8',
                       '9', '10', 'King', 'Queen', 'Jack', 'Ace')
  
  def __init__(self, suit, value):
    
    if suit.title() not in Card.possible_suits:
      
      raise ValueError('Suit must be: {}'.format(Card.possible_suits))
    
    else:
      
        self.suit = suit
        
    if value.title() not in Card.possible_values:
        
      raise ValueError('Value must be: {} and must be a string.'.format(Card.possible_values))
        
    else:
        
      self.value = value
      
    red = ('Diamond', 'Heart')
    
    black = ('Club', 'Spade')
      
    if self.suit in red:
      
      self.color = 'Red'
      
    else:
      
      self.color = 'Black'
      
  def __str__(self):
      
    return '{} of {}s'.format(self.value, self.suit)
        
  def __lt__(self, other):
    
    index1 = self.value
    index2 = other.value
    
    # Takes the value and finds the index number with it.
    # This number is used to compare and see which is smaller.
    # A similar method is used for all standard operators.
    
    result1 = Card.possible_values.index(index1)
    result2 = Card.possible_values.index(index2)
    
    return result1 < result2
    
  def __le__(self, other):
    
    index1 = self.value
    index2 = other.value
    
    result1 = Card.possible_values.index(index1)
    result2 = Card.possible_values.index(index2)
    
    return result1 <= result2
    
  def __gt__(self, other):
    
    index1 = self.value
    index2 = other.value
    
    result1 = Card.possible_values.index(index1)
    result2 = Card.possible_values.index(index2)
    
    return result1 > result2
    
  def __ge__(self, other):
    
    index1 = self.value
    index2 = other.value
    
    # Takes the value and finds the index number with it.
    # This number is used to compare and see which is smaller.
    
    result1 = Card.possible_values.index(index1)
    result2 = Card.possible_values.index(index2)
    
    return result1 >= result2
    
  def __eq__(self, other):
    
    index1 = self.value
    index2 = other.value
    
    result1 = Card.possible_values.index(index1)
    result2 = Card.possible_values.index(index2)
    
    return result1 == result2
    
        
  def __ne__(self, other):
    
    index1 = self.value
    index2 = other.value
    
    result1 = Card.possible_values.index(index1)
    result2 = Card.possible_values.index(index2)
    
    return result1 != result2
    
class Deck(object):
  
  def __init__(self):
    
    self.deck = Deck.make_deck()
  
  @classmethod
  def make_deck(cls):
  
    deck = []
  
    for suit in Card.possible_suits:
    
      for value in Card.possible_values:
      
        deck.append(Card(suit, value))
      
    return deck
  
    # Does all the work of creating 52 instances of the Card class for you!

  def shuffle_deck(self, msg = 'no'):
  
    # random.shuffle() did not return instances of the class,
    # So I created a way to shuffle the deck myself.
  
    # deck is assumed to be a list.
    # msg is an optional input. If it is not 'no', a message
    # will print that says the deck was shuffled.
  
    shuffled_deck = []
  
    while len(self.deck) > 0:
    
      card_in_deck = random.randint(0, len(self.deck) - 1)
      # A random card is chosen by getting a random index number.
    
      card = self.deck.pop(card_in_deck)
      # That index number is used with pop() to remove it
      # from the deck
    
      shuffled_deck.append(card)
      # It's then added to the shuffled deck until the original
      # list is empty
    
    self.deck = shuffled_deck
    
    if msg != 'no':
      
      print('Deck has been shuffled!')

  def __str__(self):
    
    print_deck = []
    
    for card in self.deck:
      
      print_deck.append(str(card))
      
    return '{}'.format(print_deck)
    
  