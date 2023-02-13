from __future__ import annotations

class StringBuilder:
    # Optional argument for a string and a capacity (optional). 
    # Otherwise defaults to an empty string and has no limit on characters.
    def __init__(self, string = "", capacity = None):
        pass 
  
    # Returns the string that is built.
    def __str__(self) -> str:
        pass
  
    # Appends s to the array in O(len(s)) at the end. 
    # Should raise an exception if over capacity.
    def append(self, s: str) -> None: 
        pass
  
    # Returns the length of the string.
    def size(self) -> int:
        pass
    
    # Returns the character at location index. 
    def char_at(self, index: int) -> str:
        pass
    
    # Deletes characters between start (inclusive) and end (exclusive). 
    # Should raise an exception if start, end are out of bounds.
    def delete(self, start: int, end = None) -> None:
        pass

    # Returns a substring from indices start to end. 
    # Should raise an exception if start, end are out of bounds.
    def substring(self, start: int, end = None) -> str:
        pass

    # Reverses the current string
    def reverse(self) -> str:
        pass

    # Replaces all occurrences of “old” with “new” 
    def replace(self, old: str, new: str):
        pass