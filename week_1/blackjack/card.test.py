import unittest
from card import Card

class TestK1( unittest.TestCase ):
  def setUp( self ):
    self.card = Card( 'Clubs', 'Jack' )

  def test_suit( self ):
    self.assertEqual( 
      self.card.get_suit(), 
      'Clubs' 
    )

  def test_value( self ):
    self.assertEqual( 
      self.card.get_value(), 
      'Jack' 
    )    

  def test_str( self ):
    self.assertEqual( 
      self.card.__str__(), 
      'Jack of Clubs' 
    )


if __name__ == '__main__':
  unittest.main()