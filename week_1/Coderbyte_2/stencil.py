from __future__ import annotations

'''
Below is a Dog class that inherits from Animal. 
Each Animal can "talk" which returns a string based on its name.
'''

class Animal:
    def __init__(self, name: str, weight: int) -> None:
        self.name = name
        self.weight = weight

    def talk(self) -> str:
        return f'My name is {self.name}'

    def get_weight(self) -> int:
        return self.weight

class Dog(Animal):
    def talk(self) -> str:
        return f'Woof. My name is {self.name}'

'''
Perform the following tasks. 

(1) Write a Bird class that inherits from Animal and will say "Chirp" before saying its name.
(2) Write a Duck that inherits from Bird. Instead of "Chirp" it will say "Quack"
'''

class Bird(Animal):
    def talk(self) -> str:
      return f'Chirp. My name is {self.name}'

class Duck(Bird):
    def talk(self) -> str:
      return f'Quack. My name is {self.name}'