def fn_a(n: int) -> int:
  if n == 1:
    return n
  return fn_a(n - 1) + 1

def fn_b(n: int) -> int:
  if n == 1:
    return n
  return fn_b(n - 1) + fn_b(n-1)

def fn_c(n: int) -> int:
  if n == 1:
    return n
  return fn_c(n - 1) * n

def fn_d(n: int) -> int:
  if n <= 1:
    return 1
  count = 0
  for i in range(n):
    count += i
  return fn_d(n//2) + fn_d(n // 2) + count

def fn_e(n: int) -> int:
  if n == 0:
    return 1
  return fn_e(n // 2) + fn_e(n // 2)

def fn_f(n: int) -> int:
  if n + 1 < 0:
    return n
  return fn_f(n // 2) + fn_f(n // 2)

def fn_g(n: int, m: int) -> int:
    if n <= 0 or m <= 0:
        return 1
    return fn_g(n//2, m) + fn_g(n, m//2)


print('fn_a')
print(fn_a(2))
print(fn_a(4))
print(fn_a(8))
print(fn_a(16))

print('')
print('fn_b')
print(fn_b(2))
print(fn_b(4))
print(fn_b(8))
print(fn_b(16))

print('')
print('fn_c')
print(fn_c(2))
print(fn_c(4))
print(fn_c(8))
print(fn_c(16))

print('')
print('fn_d')
print(fn_d(2))
print(fn_d(4))
print(fn_d(8))
print(fn_d(16))

print('')
print('fn_e')
print(fn_e(2))
print(fn_e(4))
print(fn_e(8))
print(fn_e(16))

print('')
print('fn_g')
print(fn_g(1,1))
print(fn_g(2,2))

print(fn_g(2,0))
print(fn_g(0,2))

print(fn_g(1,0))
print(fn_g(0,1))
