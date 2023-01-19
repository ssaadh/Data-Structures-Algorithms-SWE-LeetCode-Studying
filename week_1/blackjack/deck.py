import random
from card import Card

class Deck:    
  # Creates a sorted deck of playing cards. 13 values, 4 suits.
  # You will iterate over all pairs of suits and values to add them to the deck.
  # Once the deck is initialized, you should prepare it by shuffling it once.
  def __init__(self):
    SUITS = ["Diamonds", "Spades", "Hearts", "Clubs"]
    VALUES = ["Ace", "Two" , "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
    self.reset()
  
  def __reset_deck( self ):
    self.deck = []
    for suit in SUITS:
      for value in VALUES:
        new_card = Card( suit, value )
        self.deck.append( new_card )

  # Returns the number of Cards in the Deck
  def get_size(self):
    return len( self.deck )

  def get_deck( self ):
    return self.deck
  
  # Shuffles the deck of cards. This means randomzing the order of the cards in the Deck.
  def shuffle(self):
    for i in range( len( self.get_size() ) ):
      shuffle_one_card( i )

  # Value has to change. Not a true shuffle, possibly?
  def shuffle_one_card( self, index ):
    tmp = self.deck[ index ]
    swap = index
    while index === swap:
      swap = random.randint( 0, self.get_size() )
    self.deck[ index ] = self.deck[ swap ]
    self.deck[ swap ] = tmp
  
  # Returns the top Card in the deck, but does not modify the deck.
  def peek(self):
    return self.deck[ 0:1 ]
  
  # Removes and returns the top card in the deck. The card should no longer be in the Deck.
  def draw(self):
    return self.deck.pop( 0 )
    # top_card = self.peek()
    # self.deck = self.deck.pop( 0 )
    # return top_card
  
  # Adds the input card to the deck. 
  # If the deck has more than 52 cards, do not add the card and raise an exception.
  def add_card(self, card):
    if self.get_size() > 52:
      # @TODO how to do an exception?
      exception( 'Deck full' )
    self.deck.append( card )
  
  # Calling this function should print all the cards in the deck in their current order.
  def print_deck(self):
    lst = ''
    for i in self.deck:
      lst += i.__str__ + ', '
    return lst
    
  # Resets the deck to it's original state with all 52 cards.
  # Also shuffle the deck.
  def reset(self):
    self.__reset_deck()
    self.shuffle()

