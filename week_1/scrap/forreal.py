# Pass by value 
def increment(x): 
  x += 1 
  y = 10 

increment(y) 
print(y) # Output: 10 

# Pass by reference 
def increment(x): 
  x[0] += 1 
  y = [10] 

increment(y) 
print(y[0]) # Output: 11 