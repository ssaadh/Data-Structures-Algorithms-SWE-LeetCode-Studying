# def fn_b(n: int) -> int:
#   if n == 1:
#     return n
#   k = fn_b(n - 1) + fn_b(n - 1)
#   # print(k)
#   return k

# def fn_d(n: int) -> int:
#   if n <= 1:
#     return 1
#   count = 0
#   for i in range(n):
#     count += i
#   print('count: ' + str(count))
#   kj = fn_d(n // 2) + fn_d(n // 2) + count
#   print('kj:' + str(kj))
#   return kj

# print('')
# print('fn_b')
# print(fn_b(2))
# print(fn_b(4))
# print(fn_b(8))
# print(fn_b(16))

# print('')
# print('fn_d')
# print(fn_d(2))
# print(fn_d(4))
# print(fn_d(8))
# print(fn_d(16))

# l = [(1,2), (2,1), (1,3)]
# l.sort()
# print(l)

class Something:
  def __init__(self, x: int, y: int) -> None:
    self.x = x
    self.y = y

  def __gt__(self, other):
    return self.x > other.x

l = [Something(1,2), Something(3,4), Something(5,6)]
l.sort()
for i in l:
  print(i.x)

my_string = 'hello world'
print(','.join(my_string.split()))
		
def ff(n: int) -> bool:
  if n < 0:
      return True
  if n < 3:
      return n == 0
  return ff(n - 3) and ff(n - 6)

print(ff(9))

class A:
  def __init__(self, x, y):
    self.x = x
    self.y = y

a = A(2, 3)
print(a)

class A:
  def __init__(self, x, y):
    self.x = x
    self.y = y


  def f(self, x):
    return x*2

a = A(2, 3)
print(a.f(5))

class A:
  def __init__(self, x, y):
    self.x = x
    self.y = y


  def f(self, x):
    return x * 2


class B(A):
  def g(self, y):
    return self.f(y) + 4
		
		
b = B(2, 3)
print(b.g(5))

def f(m: int, n : int) -> int:
  if min(m, n) <= 1:
    return 0
  return f(m // 2, n - 1) * f(m - 1, n//2) + m * n

print(f(5, 7))

def flatten(lst):
  result = []
  for i in range(len(lst)):
    if type(lst[i]) == list:
      result += flatten(lst[i])
  else:
    result.append(lst[i])
  return result

print(flatten([1, [2, [3, 4], 5], 6]))
