from stencil import *

woodstock = Bird("Woodstock", 10)
daffy = Duck("Daffy", 20)

def test_bird_1():
    assert woodstock.get_weight() == 10

def test_bird_2():
    assert woodstock.talk() == "Chirp. My name is Woodstock"

def test_duck_1():
    assert daffy.get_weight() == 20

def test_duck_2():
    assert daffy.talk() == "Quack. My name is Daffy"