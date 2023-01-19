from numpy import insert
import stdio
import stddraw
from tour import Tour
from point import Point

def insertHeuristics():
    # get dimensions
    width = stdio.readInt()
    height = stdio.readInt()
    border = 20
    stddraw.setCanvasSize( width, height + border )
    stddraw.setXscale( 0, width )
    stddraw.setYscale( -border, height )

    # run smallest insertion heuristic
    tour = Tour()
    while not stdio.isEmpty():
        x = stdio.readFloat()
        y = stdio.readFloat()
        p = Point( x, y )
        # tour.insertNearest( p )
        tour.insertSmallest( p )

    # draw to standard draw
    tour.draw()
    stddraw.show()

    # prtour to standard output
    stdio.writeln( tour )
    stdio.writef( "Tour distance = %.4f\n", tour.distance() )
    stdio.writef( "Number of points = %d\n", tour.size() )

if __name__ == "__main__":
    # tsp2.txt tsp3.txt tsp10.txt tsp100.txt
    # tsp1000.txt
    # tsp85900.txt
    # mona-50k.txt mona-100k.txt    
    # germany15112.txt usa13509.txt

    insertHeuristics()
