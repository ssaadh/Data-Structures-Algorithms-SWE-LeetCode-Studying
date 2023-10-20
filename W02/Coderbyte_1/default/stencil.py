from __future__ import annotations

class Node:
  def __init__(self, val: int, next_node: Node) -> None:
    self.val = val
    self.next_node = next_node 

'''
Write a function to insert into the front a LinkedList and returns the head.
'''
def insert_front(head: Node, val: int) -> Node:
  pass

'''
Write a function that returns a string representation of the list.
Format-wise, for an input Node(1, Node(2, Node(3, None))) you must return
1 -> 2 -> 3
'''
def str_list(head: Node) -> str:
  pass

'''
Write a function that inserts to the end of a linked list and returns the head.
'''
def insert_end(head: Node, val: int) -> Node:
  pass

'''
Write a function that returns the size of the linked list
'''
def get_size(head: Node) -> int:
  pass

'''
Write a function that determines if a linked list has a cycle, given the head of the list.
'''
def has_cycle(head: Node) -> bool:
  pass

'''
Given the head of a circular linked list, write a method to sum all elements of the list up. 
Assume all the values of the node are integers.
'''
def get_circular_list_sum(head: Node) -> int:
  pass
