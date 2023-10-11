def freq(s):
   my_dict = dict()
   arr = []
   for c in s:
      if c in my_dict: 
         my_dict[c] += 1
      else:
         my_dict[c] = 1
   return my_dict 

print(freq('aabbcc'))

