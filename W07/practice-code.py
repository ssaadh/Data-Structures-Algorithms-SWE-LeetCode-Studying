def unique_paths(m: int, n: int) -> int:
  return _unique_paths(0, 0, m, n)

def _unique_paths(i: int, j: int, m: int, n: int) -> int:
  if i > m or j > n:
    return 0
  if i == (m - 1) and j == (n - 1):
    return 1
  return _unique_paths(i + 1, j, m, n) + _unique_paths(i, j + 1, m, n)


print(unique_paths(0,3)) # 0
print(unique_paths(3,0)) # 0
print('--')
print(unique_paths(0,2)) # 0
print(unique_paths(2,0)) # 0
print('--')
print(unique_paths(0,0)) # 0
print(unique_paths(0,1)) # 0
print(unique_paths(1,0)) # 0
print('--')

print(unique_paths(1,1)) # 1
print('-')
print(unique_paths(1,2)) # 1
print('-')
print(unique_paths(2,1)) # 1
print('-')
print(unique_paths(2,2)) # 2
print('-')

print(unique_paths(1,3)) # 1
print('-')
print(unique_paths(3,1)) # 1
print('-')
print(unique_paths(2,3)) # 3
print('-')
print(unique_paths(3,2)) # 3
print('-')
print(unique_paths(3,3)) # 6
print('-')
