from deck import Deck

class Blackjack:
  # Creates a Blackjack game with a new Deck.
  def __init__(self):
    self.deck = Deck()
    self.hand = []
    
  # Computes the score of a hand. 
  # For examples of hands and scores as a number.
  # 2,5 -> 7
  # 3, 10 -> 13
  # 5, King -> 15
  # 10, Ace -> 21
  # 10, 8, 4 -> Bust so return -1
  # 9, Jack, Ace -> 20 
  # If the Hand is a bust return -1 (because it always loses)
  def _get_score(self, hand: List[Card]) -> int:
    scores = { 
      "Ace": 1, "Two": 2 , "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10 
    }
    sum = 0
    aces = false
    # Total cards together
    for acard in hand:
      if acard.value == 1:
        aces = true
      sum += scores[ acard.value ]
    # Bust
    if sum > 21:
      return -1
    # Ace part
    if aces is True:
      if sum + 10 === 21:
        return 21
      if sum + 10 < 21:
        return sum + 10
    # Finally
    return sum      
    
  
  # Prints the current hand and score.
  # E.g. would print out (Ace of Clubs, Jack of Spades, 21)
  # E.g. (Jack of Clubs, 5 of Diamonds, 8 of Hearts, "Bust!")
  def _print_current_hand(self, hand):
    total = ''
    for a_card in hand:
      total += a_card.__str__ + ', '
    score = _get_score( hand )
    if score == -1:
      return total + '"Bust!"'
    return total + str( score )
  

  # The previous hand is discarded and shuffled back into the deck.  
  # Should remove the top 2 cards from the current deck and   
  # Set those 2 cards as the "current hand". 
  # It should also print the current hand and score of that hand.
  # If less than 2 cards are in the deck, 
  # then print an error instructing the client to shuffle the deck.
  def deal_new_hand( self ):
    # The previous hand is discarded and shuffled back into the deck.
    # ME: What does shuffle back into deck mean?
    for card in self.hand:
      self.deck.append( card )
      self.deck.shuffle_one_card( len( self.deck.size ) - 1 )
    self.hand = []

    # If less than 2 cards are in the deck, 
    # then print an error instructing the client to shuffle the deck.
    if self.deck.size < 2:
      print( 'error', 'Deck almost empty. Shuffle the deck.' )
    
    # Should remove the top 2 cards from the current deck and   
    # Set those 2 cards as the "current hand". 
    for twice in range( 2 ):
      new_card = self.deck.draw()
      self.hand.append( new_card )

    # It should also print the current hand and score of that hand.
    _print_current_hand( self.hand )
    

  # Deals one more card to the current hand and prints the hand and score.
  # If no cards remain in the deck, print an error.
  def hit( self ): 
    if self.deck.size <= 0:
      # @TODO is there a specific way to print an error?
      print( 'error: no deck left' )

    new_card = self.deck.draw()
    self.hand.append( new_card )
    _print_current_hand( self.hand )
      
  
  # Reshuffles all cards in the "current hand" and "discard pile"
  # and shuffles everything back into the Deck.
  def reshuffle(self):
    self.hand = []
    self.deck.reset()
      