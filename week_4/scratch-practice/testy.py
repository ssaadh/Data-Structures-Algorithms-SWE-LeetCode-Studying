def fun(m: int, n: int) -> int:
  if min(m, n) <= 1:
    return 0
  return fun(m // 2, n - 1) * fun(m - 1, n//2) + m * n

print(fun(5, 7))
# f(2, 6) * f(4, 3) + m * n

# f(2, 6) = f(1, 5) * f(1, 3) + 2 & 6 = 0 * 0 + 12 = 12
# f(4, 3) = f(2, 2) * f(3, 1) + 4 * 3 = 12

#12 * 12 + 5 * 7 = 144 + 35 = 179