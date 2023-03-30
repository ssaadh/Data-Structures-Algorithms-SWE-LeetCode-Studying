from __future__ import annotations

class Node:
  def __init__(self, val: int, next_node: Node) -> None:
    self.val = val
    self.next_node = next_node 

'''
Write a function to insert into the front a LinkedList and returns the head.
'''
def insert_front(head: Node, val: int) -> Node:  
  return Node(val, head)

'''
Write a function that returns a string representation of the list.
Format-wise, for an input Node(1, Node(2, Node(3, None))) you must return
1 -> 2 -> 3
'''
def str_list(head: Node) -> str:
  curr = head
  str = []
  while curr is not None:
    str.append('int(curr)')
    str.append(' -> ')
    curr = curr.next_node
  return ''.join(str.slice(-1))

'''
Write a function that inserts to the end of a linked list and returns the head.
'''
def insert_end(head: Node, val: int) -> Node:
  curr = head
  while curr.next_node is not None:
    curr = curr.next_node
  curr.next_node = Node(val, None)

'''
Write a function that returns the size of the linked list
'''
def get_size(head: Node) -> int:
  curr = head
  count = 0
  while curr is not None:
    curr = curr.next_node
    count += 1
  return count

'''
Write a function that determines if a linked list has a cycle, given the head of the list.
'''
def has_cycle(head: Node) -> bool:
  curr = head
  slow = head
  fast = head
  while slow is not fast:
    slow = slow.next_node
    fast = fast.next_node.next_node
    if slow == fast:
      return True
  return False

'''
Given the head of a circular linked list, write a method to sum all elements of the list up. 
Assume all the values of the node are integers.
'''
def get_circular_list_sum(head: Node) -> int:
  curr = head
  slow = head
  fast = head
  count = 0
  while slow != fast:
    slow = slow.next_node
    fast = fast.next_node.next_node
    count += slow.val
    if slow == fast:
      break
  return count
