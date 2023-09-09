from node import Node

def bt_first():
  root = Node(100)
  root.left = Node(50)
  root.left.left = Node(25)
  root.left.left.left = Node(20)
  root.left.left.right = Node(30)
  root.left.right = Node(75)
  root.left.right.left = Node(60)
  root.left.right.right = Node(80)
  root.right = Node(200)
  root.right.left = Node(190)
  root.right.left.left = Node(180)
  root.right.left.left.left = Node(170)
  root.right.left.left.right = Node(181)
  root.right.right = Node(500)
  root.right.right.right = Node(550)
  root.right.right.right.left = Node(525)
  root.right.right.right.right = Node(575)
  return root

def bt_second():
  root = Node(1)    
  root.left = Node(2)
  root.left.left = Node(4)
  root.left.left.left = Node('4L')
  root.left.left.right = Node('4R')
  root.left.right = Node('2R')
  root.left.right.left = Node('2RL')
  root.left.right.right = Node('2RR')

  root.right = Node(3)
  root.right.left = Node('3L')
  root.right.right = Node(5)
  root.right.right.left = Node(6)
  root.right.right.left.left = Node('6L')
  root.right.right.left.right = Node('6R')
  root.right.right.right = Node(7)
  root.right.right.right.left = Node('7L')
  root.right.right.right.right = Node(8)
  return root

def bt_long_legs():
  root = Node(1)
  root.left = Node(2)
  # root.left.left = Node(25)
  # root.left.left.left = Node(20)
  # root.left.left.right = Node(30)
  # root.left.right = Node(75)
  # root.left.right.left = Node(60)
  # root.left.right.right = Node(80)
  root.right = Node(3)
  root.right.left = Node(4)
  root.right.left.left = Node(6)
  root.right.left.left.left = Node(8)
  root.right.left.left.right = Node(10)
  root.right.left.left.left.left = Node(12)
  root.right.right = Node(5)
  root.right.right.right = Node(7)
  root.right.right.right.left = Node(9)
  root.right.right.right.right = Node(11)
  root.right.right.right.right.right = Node(13)
  return root

def bt_a():
  root = Node(8)
  root.left = Node(3)
  root.left.left = Node(1)
  root.left.right = Node(6)
  root.left.right.left = Node(4)
  root.left.right.right = Node(7)

  root.right = Node(10)
  root.right.right = Node(14)
  root.right.right.left = Node(12)
  return root

def bt_b():
  root = Node(1)
  root.right = Node(2)
  root.right.right = Node(3)
  root.right.right.right = Node(4)
  root.right.right.right.right = Node(5)
  return root

def bt_c():
  root = Node(1)
  root.left = Node(2)
  root.left.left = Node(4)
  root.left.left.left = Node(8)
  root.left.left.right = Node(9)

  root.left.right = Node(5)
  root.left.right.left = Node(10)
  root.left.right.right = Node(11)

  root.right = Node(3)
  root.right.left = Node(6)
  root.right.right = Node(7)
  return root

def bt_d():
  root = Node(1)
  root.left = Node(2)
  root.left.left = Node(4)
  root.left.right = Node(5)

  root.right = Node(2)
  root.right.left = Node(5)
  root.right.right = Node(4)    
  return root

def bt_e():
  root = Node(1)
  root.left = Node(2)
  root.left.left = Node(4)
  root.left.right = Node(5)
  root.left.left.left = Node(10)

  root.right = Node(3)
  root.right.right = Node(6)
  root.right.right.right = Node(8)
  root.right.right.right.right = Node(9)
  return root
