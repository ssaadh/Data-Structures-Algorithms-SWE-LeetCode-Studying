class Node:
  def __init__(self, val, prev = None, next = None):
    self.val = val
    self.prev = prev
    self.next = next

class BrowserHistory:
  # Initializes browser hisotry from new tab. 
  # By default the starting URL will be an empty string.
  def __init__(self): 
      self.curr = Node( '' )
  
  # Returns the url of the current page.
  def current_page(self):
      return self.curr.val
  
  # Navigates to the "page" from the current page. 
  # Nagivating forward should overwrite all previous forward browser history.
  def go_to(self, page): 
      tmp = self.curr
      new_node = Node( page )
      # the old/current pointer
      tmp.next = new_node
      # now this is the new_node at pointer
      self.curr = new_node
      # setting new_node's and now the pointer prev
      self.curr.prev = tmp
  
  # Navigates to the previous page visited.
  # After navigating return the URL of the current page.
  def go_back(self):
      self.curr = self.curr.prev
      return self.curr.val
    
  # Navigates to the page ahead in browser history.
  # If there is no page ahead, do nothing.
  # After navigating return the URL of the current page.
  def go_forward(self):
      if self.curr.next is not None:
        self.curr = self.curr.next
        return self.curr.val
  
  # Navigates backwards N pages in browser history.
  # If there are not N pages behind, then return the new tab URL which is an empty string.
  # After navigating return the URL of the current page.
  def skip_backward(self, N):
      for i in range( N ):
          if self.curr.prev is None:
              return ''
          self.curr = self.curr.prev
      return self.curr.val

  def skip_backward_instructions(self, N):
      for i in range( N ):
          if self.curr.prev is None:
              break
          self.curr = self.curr.prev
      return self.curr.val

  # Navigates forward N pages in browser history.
  # If there are not N pages ahead, then go as far as you can.
  # After navigating return the URL of the current page.
  def skip_forward(self, N):
      for i in range( N ):
          if self.curr.next is None:
              break
          self.curr = self.curr.next
      return self.curr.val

  def asList( self ):
    forward = []
    back = []
    curr = self.curr
    while curr:
      forward.append( curr.val )
      curr = curr.next
    curr = self.curr
    while curr.prev:
      curr = curr.prev
      back.append( curr.val )
    return [ forward, back ]

