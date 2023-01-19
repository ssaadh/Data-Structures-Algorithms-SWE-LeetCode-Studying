from math import sqrt
import stddraw

class Point:
    # create the Point (x, y) in 2D
    def __init__( self, x, y ):
        self.x = x
        self.y = y
    
    # return a reasonable string representation of the Point.
    def toString( self ):
        str_x = str( self.x )
        str_y = str( self.y )
        return ( 
            "(%s, %s)" % 
            ( str_x, str_y )
        )

    # Draw point using standard draw
    def draw( self ):
        stddraw.point( self.x, self.y )

    # Draw a line segment between the two points with stddraw.
    def drawTo( self, that ):
      stddraw.line( 
        self.x, self.y, 
        that.x, that.y 
      )

    # Return Euclidean distance between the two points.
    def distanceTo( self, that ):
        return sqrt( 
            ( self.x - that.x ) ** 2 + 
            ( self.y - that.y ) ** 2 
        )
