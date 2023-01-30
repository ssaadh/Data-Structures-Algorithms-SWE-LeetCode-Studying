def factorial(n):
  if n == 0 or n == 1:
    print('base')
    return 1
  hi = factorial(n-1) * n
  print(hi)
  return hi

# print(factorial(5))


def fn_i(lst):
  totes = ''
  for i in lst:
    totes += str(i)
  return totes


print(fn_i([1, 2, 3, 4, 5]))

def fn_r(lst, n, totes):  
  if n == 0:
    return str(lst[n])
  return fn_r(lst, n-1, totes) + str(lst[n])

print(fn_r([1,2,3,4,5], 4, ''))