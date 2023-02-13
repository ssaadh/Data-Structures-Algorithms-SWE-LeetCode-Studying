from stencil import *

def test_fizz_buzz_1():
  assert fizz_buzz(15) == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "Fizz Buzz"]

def test_max_integer_1():
  assert max_integer([4, 6, 8, 2, 7]) == 8

def test_max_integer_index_1():
  assert max_integer_index([4, 6, 8, 2, 7]) == 2

def test_max_integer_index_2():
  assert max_integer_index([4, 6, 8, 2, 8]) == 2

def test_tuples_to_dictionary_1():
  assert tuples_to_dictionary([("Alice", 57), ("Bob", 62), ("Carl", 73)]) == {"Alice": 57, "Bob": 62, "Carl": 73}

def test_tuples_to_dictionary_2():
  assert tuples_to_dictionary([("Alice", 57), ("Bob", 62), ("Alice", 73)]) == {"Alice": 73, "Bob": 62} 

def test_highest_scoring_students_1():
  assert highest_scoring_students({"Alice": 100, "Bob": 90}) == ["Alice"]
    
def test_highest_scoring_students_2():
  assert highest_scoring_students({"Alice": 100, "Bob": 100}) == ["Alice", "Bob"]
    
def test_count_score_frequencies_1():
  assert count_score_frequencies({"Alice": 100, "Bob": 90, "Carl": 90}) == {100: 1, 90: 2} 

def test_average_score_1():
  assert average_score({"Alice": 100, "Bob": 90, "Carl": 90, "Dave": 90}) == 92.5

def test_average_score_frequency_weighted_1():
  assert average_score_frequency_weighted({100: 1, 90: 3}) == 92.5 

def test_convert_to_gradebook_1():
  assert convert_to_gradebook({"Alice": 100, "Bob": 89, "Carl": 79, "Dave": 60, "Eve": 50}) == {"A": 1, "B": 1, "C": 1, "F": 2}