import unittest
from browser_history import BrowserHistory

class TestK1( unittest.TestCase ):
    def setUp( self ):
      self.history = BrowserHistory()

    def test_step_01( self ):
      print( '01) ', self.history.asList() )

      self.assertEqual( 
        self.history.current_page(), 
        '' 
      )
        
    def test_step_02( self ):
      result = self.history.go_to("leetcode.com") 
      print( '02) ', self.history.asList() )

      self.assertEqual( 
        self.history.current_page(), 
        'leetcode.com' 
      )

    def test_step_03( self ):
      result = self.history.go_to("leetcode.com") 
      result = self.history.go_to("google.com") 
      print( '03) ', self.history.asList() )
      self.assertEqual( 
        self.history.current_page(), 
        'google.com' 
      )

    def test_step_04( self ):
      result = self.history.go_to("leetcode.com") 
      result = self.history.go_to("google.com") 
      result = self.history.go_to("facebook.com") 
      print( '04) ', self.history.asList() )

      self.assertEqual( 
        self.history.current_page(), 
        'facebook.com' 
      )

    def test_step_05( self ):
      result = self.history.go_to("leetcode.com") 
      result = self.history.go_to("google.com") 
      result = self.history.go_to("facebook.com") 
      result = self.history.go_to("youtube.com") 
      print( '05) ', self.history.asList() )

      self.assertEqual( 
        self.history.current_page(), 
        'youtube.com' 
      )

    def test_step_06( self ):
      result = self.history.go_to("leetcode.com") 
      result = self.history.go_to("google.com") 
      result = self.history.go_to("facebook.com") 
      result = self.history.go_to("youtube.com") 
      result = self.history.go_back()
      print( '06) ', self.history.asList() )

      self.assertEqual( 
        self.history.current_page(), 
        'facebook.com' 
      )

    def test_step_07( self ):
      result = self.history.go_to("leetcode.com") 
      result = self.history.go_to("google.com") 
      result = self.history.go_to("facebook.com") 
      result = self.history.go_to("youtube.com") 
      result = self.history.go_back()
      result = self.history.go_back()
      print( '07) ', self.history.asList() )

      self.assertEqual( 
        self.history.current_page(), 
        'google.com' 
      )

    def test_step_08( self ):
      result = self.history.go_to("leetcode.com") 
      result = self.history.go_to("google.com") 
      result = self.history.go_to("facebook.com") 
      result = self.history.go_to("youtube.com") 
      result = self.history.go_back()
      result = self.history.go_back()
      result = self.history.go_forward()
      print( '08) ', self.history.asList() )

      self.assertEqual( 
        self.history.current_page(), 
        'facebook.com' 
      )

    def test_step_09( self ):
      result = self.history.go_to("leetcode.com") 
      result = self.history.go_to("google.com") 
      result = self.history.go_to("facebook.com") 
      result = self.history.go_to("youtube.com") 
      result = self.history.go_back()
      result = self.history.go_back()
      result = self.history.go_forward()
      result = self.history.go_to("linkedin.com") 
      print( '09) ', self.history.asList() )

      self.assertEqual( 
        self.history.current_page(), 
        'linkedin.com' 
      )

    def test_step_10( self ):
      result = self.history.go_to("leetcode.com") 
      result = self.history.go_to("google.com") 
      result = self.history.go_to("facebook.com") 
      result = self.history.go_to("youtube.com") 
      result = self.history.go_back()
      result = self.history.go_back()
      result = self.history.go_forward()
      result = self.history.go_to("linkedin.com") 
      result = self.history.skip_forward( 2 )
      print( '10) ', self.history.asList() )

      self.assertEqual( 
        result, 
        'linkedin.com' 
      )

    def test_step_11( self ):
      result = self.history.go_to("leetcode.com") 
      result = self.history.go_to("google.com") 
      result = self.history.go_to("facebook.com") 
      result = self.history.go_to("youtube.com") 
      result = self.history.go_back()
      result = self.history.go_back()
      result = self.history.go_forward()
      result = self.history.go_to("linkedin.com") 
      result = self.history.skip_forward( 2 )
      result = self.history.skip_backward( 2 )
      print( '11) ', self.history.asList() )

      self.assertEqual( 
        result, 
        'google.com' 
      )

    def test_step_12( self ):
      result = self.history.go_to("leetcode.com") 
      result = self.history.go_to("google.com") 
      result = self.history.go_to("facebook.com") 
      result = self.history.go_to("youtube.com") 
      result = self.history.go_back()
      result = self.history.go_back()
      result = self.history.go_forward()
      result = self.history.go_to("linkedin.com") 
      result = self.history.skip_forward( 2 )
      result = self.history.skip_backward( 2 )
      result = self.history.skip_backward( 7 )
      print( '12) ', self.history.asList() )

      self.assertEqual( 
        result, 
        '' 
      )

    def test_step_12_instructions( self ):
      result = self.history.go_to("leetcode.com") 
      result = self.history.go_to("google.com") 
      result = self.history.go_to("facebook.com") 
      result = self.history.go_to("youtube.com") 
      result = self.history.go_back()
      result = self.history.go_back()
      result = self.history.go_forward()
      result = self.history.go_to("linkedin.com") 
      result = self.history.skip_forward( 2 )
      result = self.history.skip_backward( 2 )
      result = self.history.skip_backward_instructions( 7 )
      result = self.history.skip_forward( 1 )
      print( '12alt) ', self.history.asList() )

      self.assertEqual( 
        result, 
        'leetcode.com' 
      )

if __name__ == '__main__':
  unittest.main()
