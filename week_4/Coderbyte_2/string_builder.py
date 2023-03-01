from __future__ import annotations

class StringBuilder:
    # Optional argument for a string and a capacity (optional). 
    # Otherwise defaults to an empty string and has no limit on characters.

    def __init__(self, string = "", capacity = None):
        self.s = string
        for c in self.s:
          self.copy.append(c)
        self.capacity = capacity
  
    # Returns the string that is built.
    def __str__(self) -> str:
        return ''.join(self.copy)
  
    # Appends s to the array in O(len(s)) at the end. 
    # Should raise an exception if over capacity.
    def append(self, s: str) -> None: 
      length = len(s) + len(self.s)
      if self.capacity is not None and self.capacity < length:
        raise Exception
      for c in s:
        self.copy.append(c)
      return None
      
  
    # Returns the length of the string.
    def size(self) -> int:
      return len(self.copy)
    
    # Returns the character at location index. 
    def char_at(self, index: int) -> str:
        if index + 1 <= self.length:
          return self.s[index]

    def _bound_checking(self, start, end):
      return (start < end) and (0 <= start <= self.size() - 1) and (1 <= end <= self.size())
      
    # Deletes characters between start (inclusive) and end (exclusive). 
    # Should raise an exception if start, end are out of bounds.
    def delete(self, start: int, end = None) -> None:
      if end is None:
        end = self.length

      if self._bound_checking(start, end):
        for c, index in range(start, end):
          del self.copy[index]
        # self.copy = self.copy[:start] + self.copy[:end]
        return None
      else:
        raise Exception
          

    # Returns a substring from indices start to end. 
    # Should raise an exception if start, end are out of bounds.
    def substring(self, start: int, end = None) -> str:
      if end is None:
        end = self.length

      tmp = []
      if self._bound_checking(start, end):
        for c in range(start, end):
          tmp.append(c)
        return tmp
        # return self.s[start:end]
      else:
        raise Exception

    # Reverses the current string
    def reverse(self) -> str:
      copy = []
      for c in range(0,1,-1):
        copy.append(self.copy[c])
      return copy

    # Replaces all occurrences of “old” with “new” 
    def replace(self, old: str, new: str):
      s = ''.join(self.copy)
      s.replace(old, new)
      self.copy = []
      for c in s:
        self.copy.append(c)
      return None