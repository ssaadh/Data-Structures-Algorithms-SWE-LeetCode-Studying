def max_integer_index(input_list: list) -> int:
  max_index = 0
  the_max = 0
  for i, num in enumerate(input_list):
    if num > the_max:
      the_max = num
      max_index = i
  return max_index

print(max_integer_index([4, 6, 8, 2, 8]))