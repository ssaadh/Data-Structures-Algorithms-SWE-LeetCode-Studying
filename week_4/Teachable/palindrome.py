def isPalindromeSpace(self, s: str) -> bool:
  # O(N), O(N)
  new_s = ""
  #remove garbage
  for c in s:
    if c.isalnum():
      new_s += c.lower()

  return new_s == new_s[::-1]

def isPalindromeMeetInMiddle(self, s: str) -> bool:
  # O(N), O(1)
  new_s = ""
  #remove garbage
  for c in s:
    if c.isalnum():
      new_s += c.lower()

  start,end = 0,len(new_s)-1
  while(start < end):
    if new_s[start] != new_s[end]:
      return False
    start += 1
    end -= 1
  return True

def isPalindromeMerge(self, s: str) -> bool:
  # O(N), O(1)
  new_s = ""
  #remove garbage
  for c in s:
    if c.isalnum():
      new_s += c.lower()
  if len(new_s) == 0:
    return True

  #true is odd length
  n = len(new_s)
  if len(new_s) % 2:
    lo = n//2 - 1
    hi = n//2 + 1
  else:
    lo,hi = n//2-1, n//2
    if new_s[lo] != new_s[hi]:
      return False
    lo -= 1
    hi += 1
  while(lo >= 0 and hi < len(new_s)):
    if new_s[lo] != new_s[hi]:
      return False
    lo -= 1
    hi += 1
  return True
