from node import Node

class Tour:
    ###
    # Basics
    ###

    # create an empty tour
    def __init__( self ):
        self.head = None
        self.count = 0

    def get_head( self ):
        return self.head
    
    def is_empty( self ):
        if self.get_head() is None:
            return True
        else:
            return False

    # number of points on tour
    def size( self ):
        return self.count


    ###
    # Looping
    ###

    def toString( self ):
        if self.is_empty():
            return ''
        # init, first run
        curr = self.get_head()
        full_string = curr.point.toString() + '\n '
        # rest
        while curr.next != self.head:
            curr = curr.next
            full_string += curr.point.toString() + '\n '
                
        return full_string

    # draw the tour to standard draw
    def draw( self ):
        if self.is_empty():
            return False

        curr = self.get_head()
        curr.point.drawTo( curr.next.point )
        while curr.next != self.get_head():
            # curr.point.draw()
            curr = curr.next    
            curr.point.drawTo( curr.next.point )
        
    # return the total distance of the tour
    def distance( self ):
        if self.is_empty():
            return 0
        # init, first run
        curr = self.get_head()
        total = curr.point.distanceTo( curr.next.point )
        # rest
        while curr.next != self.get_head():
            curr = curr.next
            total += curr.point.distanceTo( curr.next.point )
        return total
    

    ###
    # Heuristics
    ###

    def initial_insert( self, p ):
        new_node = Node( p )
        self.head = new_node
        new_node.next = self.head
        self.count += 1

    def insert_at( self, p, insert_point ):
        new_node = Node( p )
        new_node.next = insert_point.next
        insert_point.next = new_node
        self.count += 1
        

    # insert p using nearest neighbor heuristic
    def insertNearest( self, p ):
        if self.is_empty():
            self.initial_insert( p )
        elif self.size() == 1:
            self.insert_at( p, self.get_head() )
        else:
            # init
            curr, new_node = self.get_head(), Node( p )
            least_node, least_distance = self.get_head(), float( 'inf' )

            # first run
            difference = new_node.point.distanceTo( curr.point )            
            if least_distance > difference:
                least_distance, least_node = difference, curr
            # loop
            while curr.next != self.head:
                curr = curr.next
                difference = new_node.point.distanceTo( curr.point )
                if least_distance > difference:
                    least_distance, least_node = difference, curr
                
            # insert the new node
            self.insert_at( p, least_node )
    

    def smallest_diff( self, curr, new_node ):
      # difference between the two inserts
      initial = curr.point.distanceTo( curr.next.point )
      # subtract original distance, add 2 new distances
      new_distance = curr.point.distanceTo( new_node.point )
      new_distance += new_node.point.distanceTo( curr.next.point )
      return new_distance - initial

    # insert p using smallest increase heuristic
    # insert the new node after every node. subtract distance between the original and original next node
    # add distance of original node to new node + new node to original next node
    def insertSmallest( self, p ):
      if self.is_empty():
          self.initial_insert( p )
      elif self.size() == 1:
          self.insert_at( p, self.get_head() )
      else:
          # init
          curr, new_node = self.get_head(), Node( p )
          least_node, least_distance = self.get_head(), float( 'inf' )
          # first run
          difference = self.calculate_smallest_diff( curr, new_node )
          if ( least_distance > difference ):
              least_distance, least_node = difference, curr
          # loop
          while curr.next != self.head:
              curr = curr.next
              difference = self.calculate_smallest_diff( curr, new_node )
              if ( least_distance > difference ):
                  least_distance, least_node = difference, curr 

          # insert the new node
          self.insert_at( p, least_node )
            