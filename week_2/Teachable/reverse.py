class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    def __str__(self):
        cur = self
        out = ""
        while(cur):
            out += str(cur.val)
            cur = cur.next
        return out

#1 -> 2 -> 3
#3 -> 2 -> 1 -> None

# None

# 1 ->


# cur - None     <- 1  <- 2  <- 3
# prev - 3
# next = None


# cur - None
# prev - 1
# next - None

head 
-> 1 
nexty = cur.next (2)
cur.next = prev (None)
prev = cur (1)
cur = nexty (2)


3 -> 2 -> 1 -> None

def reverseLinkedList(head):
    cur = head
    prev = None
    while cur:
		  nexty = cur.next
		  cur.next = prev
		  prev = cur
		  cur = nexty

    return prev

#make List of 10 Node objects
head = Node("head")
cur = head
for i in range(10):
    cur.next = Node(i)
    cur = cur.next
print(head.next)
head.next = reverseLinkedList(head.next)
print(head.next)



def reverse(head)
  cur = head
  prev = None
  while cur:
    nexty = cur.next
    cur.next = prev

    prev = cur
    cur = nexty
  return prev


# head         1 -> 2 -> 3 -> 4 -> 5 -> None
#              -> 3 -> 4 -> 5  | 2 -> 1 -> None
# reverse head 5 -> 4 -> 3 -> 2 -> 1 -> None
# each iteration

# cur = 1

# nexty = 2
# cur.next is  2
# cur.prev is None
# prev = 1
# cur = 2
# --
# prev = 
# cur.next = 
1. Node point to None.
