import unittest
from card import Card
from deck import Deck

class TestK1( unittest.TestCase ):
  def compare_enumerables_as_diff( self, lst, lst2 ):
    flag = 0
    for i in lst:
      if i in lst2:
        flag += 1
        if flag => 2:
          return true
    return false

  def setUp( self ):
    self.deck = Deck()
    self.test_card = Card( )
  
  # shuffle
  def test_shuffle( self ):
    og_deck = self.deck.get_deck()
    self.deck.shuffle()
    self.assertTrue( 
      self.compare_enumerables_as_diff( og_deck, self.get_deck() ) 
    )

  # shuffle one card!!
  def test_shuffle_one_card( self ):
    og_deck = self.deck.get_deck()
    self.deck.shuffle_one_card( 0 )
    self.assertEqual( 
      self.get_deck()[ 0 ], 
      og_deck[ 0 ] 
    )

  def test_peek( self ):
    card = self.deck.peek()
    self.assertEqual( 
      card, 
      self.get_deck()[ 0 ] 
    )

  def test_draw( self ):
    card = self.deck.draw()
    self.assertNotEqual( 
      card, 
      self.get_deck()[ 0 ] 
    )

  def test_add_card( self ):
    initial_size = self.deck.get_size()
    self.add_card( Card( 'Clubs', 'Ace' ) )
    self.assertEqual( 
      initial_size + 1, 
      self.deck.get_size() 
    )

  # If more than 52 cards exception
  def _add_card_exception( self ):
    example_card = Card( 'Joker', 'Joker' )
    self.deck.reset()
    self.get_deck().append( example_card )
    self.assertEqual( 
      self.add_card( example_card ), 
      exception( 'Deck full' )
    )
    
  def test_print_deck( self ):
    print( self.deck.print_deck() )
    return True

  def test_reset( self ):
    for i in self.get_deck():
      self.assertIsInstance( 
        i, 
        Card 
      ) 

if __name__ == '__main__':
  unittest.main()
