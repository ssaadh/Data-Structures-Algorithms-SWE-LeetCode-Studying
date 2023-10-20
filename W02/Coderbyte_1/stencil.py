# ====================== CODING QUESTIONS ==========================
class Node:
  def __init__(self, val: int, next_node) -> None:
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
  cur = head
  stringy = str(cur.val)
  while cur.next_node is not None:
    cur = cur.next_node
    stringy += ' -> ' + str(cur.val)
  return stringy

'''
Write a function that inserts to the end of a linked list and returns the head.
'''
def insert_end(head: Node, val: int) -> Node:
  cur = head
  while cur.next_node is not None:
    cur = cur.next_node
  cur.next_node = Node(val, None)
  return head

'''
Write a function that returns the size of the linked list
'''
def get_size(head: Node) -> int:
  count = 0
  cur = head
  while cur is not None:
    cur = cur.next_node
    count += 1
  return count

'''
Write a function that determines if a linked list has a cycle, given the head of the list.
'''
def has_cycle(head: Node) -> bool:
  if head is None:
    return False
  slow = head
  fast = head.next_node
  while fast and fast.next_node:
    if slow == fast:
      return True
    slow = slow.next_node
    fast = fast.next_node.next_node
  return False

'''
Given the head of a circular linked list, write a method to sum all elements of the list up. 
Assume all the values of the node are integers.
'''
def get_circular_list_sum(head: Node) -> int:
  if head is None:
    return 0
  slow = head
  fast = head.next_node
  total = 0
  while fast and fast.next_node:
    total += slow.val
    if slow == fast:
      return total
    slow = slow.next_node
    fast = fast.next_node.next_node
  return False