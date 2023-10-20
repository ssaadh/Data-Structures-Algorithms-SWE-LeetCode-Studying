class Card:
    # Card constructor
    # The suit and value of a card, should be immutable.
    def __init__(self, suit, value):
        self.__suit = suit
        self.__value = value
    
    # Returns the suit of the card.
    def get_suit(self):
        return self.__suit

    def set_suit( self, val ):
        self.__suit = val
    
    # Returns the value of the card.
    def get_value(self):
        return self.__value

    def set_value( self, val ):
        self.__value = val
      
    # Returns a string representation of Card
    # E.g. "Ace of Spades"
    def __str__(self):
        return self.get_value() + ' of ' + self.get_suit()
