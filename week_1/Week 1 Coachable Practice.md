Free Response Questions

1. What is the difference between a class and an instance? 
A. A class is a template for creating objects. An instance is an object created from a class.

a. What is a class attribute?
A. Static variables. Universal among all instances of a class.

b. What is an instance attribute?
A. Object global variable. Specific to an initialized object of a class. Has to use self. Can be initialized in the constructor method.

2. Why do we use objects in our code? What are some of the benefits? 
A. Objects allow organizing and encapsulating code and data. Similar to functions, they can be reused and used independently. Allow for inheritance too.

3. What is the runtime of 
a) list.pop()
b) list.remove(...)
c) list.insert(..., ...)

A. (a) O(1) from end. Up to O(n) worst case in other positions
(b) O(n)
(c) O(n)


4. What does the following code block output? 
def function(a: int) -> None: 
  a = 5
a = 3
function(a)
print(a)
A. 3

5. What does the following code block output? 
def function(a: list[int]) -> None:
  a.append(5)
a = [1, 2, 3, 4]
function(a)
print(a)
A. [1, 2, 3, 4, 5]

6. Let’s say that you had this scenario of objects like a Dog and Animal class. What type of relationship would that be from an OOD sense?
A. Animal is the parent of Dog. Dog is a subclass of Animal. Heirarchal.

7. Why do we use getters/setters? Please give an example of a potential issue if you do not use them.
A. They encapsulate code. No direct access to variables. Can work with inputs or data before doing an action for the user. Potential issue is not validating things. A variable could get overwritten.

8. What is the difference between abstraction and implementation?
A. Abstraction is the encapsulation of code like a class or template for an end user like a programmer. Implementation is the practical creating of the end result code. Your own functions or objects using other libraries or code.

9. Why do we focus on the features before focusing on the implementation?
A. Multiple kinds of specific types of test driven development work better this way. Same with making a roadmap or issues/stories required for the code. This is why it helps to have a Product and/or Project Managers and/or QA devs alongside software engineers.

10. What’s wrong with the below Customer and LunchLine classes? How would you fix it?
A. 1. The line_size getter method is same as the instance variable. Can't call the getter method.
2. the type hinting doesn't work with list[Customer]. Customer is a class and isnt'er iterable via indexing. Not sure what to replace this with besides removing [Customer]
3. time isn't instantiated
