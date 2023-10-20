from __future__ import annotations

class StringBuilder:
    # Optional argument for a string and a capacity (optional). 
    # Otherwise defaults to an empty string and has no limit on characters.

    def __init__(self, string = "", capacity = None):
        self.s = string
        self.length = 0
        self.capacity = capacity
  
    # Returns the string that is built.
    def __str__(self) -> str:
        pass
  
    # Appends s to the array in O(len(s)) at the end. 
    # Should raise an exception if over capacity.
    def append(self, s: str) -> None: 
      length = len(s) + len(self.s)
      if self.capacity is not None and self.capacity < length:
        raise Exception
      self.s.append(self.s)
      self.length += length
      
  
    # Returns the length of the string.
    def size(self) -> int:
        return self.length
    
    # Returns the character at location index. 
    def char_at(self, index: int) -> str:
        if index + 1 <= self.length:
          return self.s[index]

    def _bound_checking(self, start, end):
      return (start < end) and (0 <= start <= self.capacity - 1) and (1 <= end <= self.capacity)
      
    # Deletes characters between start (inclusive) and end (exclusive). 
    # Should raise an exception if start, end are out of bounds.
    def delete(self, start: int, end = None) -> None:
      if end is None:
        end = self.length - 1

      if self._bound_checking(start, end):
        self.s = self.s[:start] + self.s[:end]
        return None
      else:
        raise Exception
          

    # Returns a substring from indices start to end. 
    # Should raise an exception if start, end are out of bounds.
    def substring(self, start: int, end = None) -> str:
      if end is None:
        end = self.length - 1
        
      if self._bound_checking(start, end):
        return self.s[start:end]
      else:
        raise Exception

    # Reverses the current string
    def reverse(self) -> str:
        pass

    # Replaces all occurrences of “old” with “new” 
    def replace(self, old: str, new: str):
        pass