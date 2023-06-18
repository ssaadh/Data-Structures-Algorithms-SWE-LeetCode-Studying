from sys import argv
from k2 import Point
import stdio
import stddraw

# Command-line takes two arguments for x and y values
def main():
    x = float( argv[ 1 ] or 4 )
    y = float( argv[ 2 ] or 3 )

    pp = Point( x, y )
    thatThere = Point( x * 2, y * 2 )

    stdio.writeln( pp.toString() )
    stdio.writeln( pp.distanceTo( thatThere ) )

    stddraw.clear( stddraw.BOOK_BLUE )
    pp.draw()
    stddraw.point(thatThere.x, thatThere.y)
    pp.drawTo( thatThere )
    stddraw.show( 1000 )

if __name__ == '__main__':
    main()
