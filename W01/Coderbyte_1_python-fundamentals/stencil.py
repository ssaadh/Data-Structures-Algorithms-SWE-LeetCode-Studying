from __future__ import annotations

'''
Write a function that appends the numbers or a string from 1 to n, inclusive, using the following rules:
1. If the number is a multiple of 3 and 5, append "Fizz Buzz"
2. If the number is just a multiple of 5, append "Buzz"
3. If the number is just a multiple of 3, append "Fizz"
4. If the number is neither a multiple of 3 nor 5, append then number as a string
'''

def fizz_buzz(n: int) -> list[str]:
  lst = [] 
  for i in range(1, n + 1):
    if i % 15 == 0:
      lst.append('Fizz Buzz')
    elif i % 3 == 0:
      lst.append('Fizz')
    elif i % 5 == 0:
      lst.append('Buzz')
    else:
      lst.append(str(i))
  return lst  

print(fizz_buzz(15))

'''
Write a function that, given a list of integers, return the largest value in the list.
'''
def max_integer(input_list: list[int]) -> int:
  # right? or does it need to be separate values, not a list
  # return max(intput_list)
  the_max = 0
  for num in input_list:
    if num > the_max:
      the_max = num
  return the_max

'''
Write a function that, given a list of integers, return the index of the largest integer in the list. 
If there are duplicates, return the earliest index.
'''
def max_integer_index(input_list: list[int]) -> int:
  max_index = 0
  the_max = 0
  for i, num in enumerate(input_list):
    if num > the_max:
      the_max = num
      max_index = i
  return max_index

'''
Write a function that, given a list of tuples in the form (Student Name, Score), returns 
a dictionary where the key is the Student Name and the value is the Score for that student.

If a Student Name appears multiple times, take the score from the tuple at the largest index.
'''
def tuples_to_dictionary(input_list: list[tuple[str, int]]) -> dict[str, int]:
  thedict = {}
  for i in input_list:
    thedict[i[0]] = i[1]
  return thedict

'''
Write a function that, given a dictionary of the form Student Name: Score, returns a list of 
names of the students who got the highest score.
In the output, student names should be sorted alphabetically ascending. 
'''
#max func
# max func
def highest_scoring_students(input_dict):
  the_list = []
  highest_score = max(input_dict.values())
  for name, score in input_dict.items():
    if score == highest_score:
      the_list.append(name)
  # sort + return
  the_list.sort()
  return the_list

# no max func -- didnt finish cuz it's silly
def highest_scoring_students_2(input_dict: dict[str, int]) -> list[int]:
  the_list = []
  highest_score = 0
  count = 0
  for name, score in input_dict.items():
    if score >= highest_score:
      highest_score = score
    if count == 0:
      # wipe the_list
      the_list = []
      the_list.append(name)
    elif count > 0:
      the_list.append(name)
  # sort + return
  the_list.sort()
  return the_list

'''
Write a function that, given a dictionary of the form Student Name: Score, returns a dictionary
of the form Score: Count. 
Suppose the input is { 'A': 100, 'B': 90, 'C': 90 }, then the output would be
{ 100: 1, 90: 2}
'''
def count_score_frequencies(input_dict: dict[str, int]) -> dict[int, int]:
  new_dict = {}
  for _, score in input_dict.items():
    if score in new_dict:
      new_dict[score] += 1
    else:
      new_dict[score] = 1
  return new_dict

'''
Write a function that, given a dictionary of the form Student Name: Score, returns the average score.
'''
# using language specific
def average_score(input_dict: dict[str, int]) -> float:
  vals = input_dict.values()
  return sum(vals) / len(vals)

# not using language specific
def average_score_2(input_dict: dict[str, int]) -> float:
  total = 0
  count = 0
  for val in input_dict.values():
    total += val
    count += 1
  return total / count

'''
Write a function that, given a dictionary of the form Score: Count, returns the average score.
'''
def average_score_frequency_weighted(input_dict: dict[int, int]) -> float:
  sum = 0
  overall_count = 0
  for score, count in input_dict.items():
    sum += (score * count)
    overall_count += count
  return sum / overall_count

'''
Write a function that, given a dictionary of the form Student Name: Score, returns a dictionary
of letter grades. Here, A is 90 to 100 inclusive, B is 80 to 89 inclusive, C is 70 to 79 inclusive, and anything else is an F.
'''
def convert_to_gradebook(input_dict: dict[str, int]) -> dict[str, int]:
  new_dict = { 'A': 0, 'B': 0, 'C': 0, 'F': 0}
  for score in input_dict.values():
    if 90 <= score <= 100:
      new_dict['A'] += 1
    elif 80 <= score <= 89:
      new_dict['B'] += 1
    elif 70 <= score <= 79:
      new_dict['C'] += 1
    else:
      new_dict['F'] += 1
  return new_dict