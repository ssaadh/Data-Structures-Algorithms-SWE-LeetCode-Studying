from stencil import * 

l1_head = Node(1, Node(2, Node(3, None)))

l2_head = Node(1, Node(2, Node(3, None)))
new_l2_head = insert_front(l2_head, 0)

l3_head = Node(1, Node(2, Node(3, None)))
new_l3_head = insert_end(l3_head, 4) 

l4_head = Node(1, None)

last_node_of_l5 = Node(3, None)
l5_head = Node(1, Node(2, last_node_of_l5))
last_node_of_l5.next_node = l5_head

def test_str_list_1():
  assert str_list(l1_head) == "1 -> 2 -> 3"

def test_str_list_2():
  assert str_list(new_l2_head) == "0 -> 1 -> 2 -> 3"

def test_str_list_3():
  assert str_list(new_l3_head) == "1 -> 2 -> 3 -> 4"

def test_get_size_1():
  assert get_size(l4_head) == 1

def test_get_size_2():
  assert get_size(l1_head) == 3

def test_has_cycle_1():
  assert has_cycle(l1_head) == False

def test_has_cycle_2():
  assert has_cycle(l5_head) == True

def test_get_circular_list_sum_1():
  assert get_circular_list_sum(l5_head) == 6