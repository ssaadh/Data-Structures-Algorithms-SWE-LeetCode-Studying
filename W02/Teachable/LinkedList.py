class Node:
    def __init__(self, item , next = None):
        self.item = item
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node("dummy")
        self._size = 0

    def __str__(self):
        #O(N) runtime
        #O(N) space
        out = ""
        cur = self.head.next
        while(cur):
            out += str(cur.item) + "|"
            cur = cur.next
        return out

    def insertFront(self, item):
        #H -> 1 -> 2      insert 3
        #H -> 3 -> 1 -> 2
        #O(1) runtime
        #O(1) space
        next = self.head.next
        self.head.next = Node(item)
        self.head.next.next = next        
        self._size += 1

    def insertFronty(self, item):
      self.head = Node(item, self.head)
      self._size += 1
      return self.head
        

    def insertLast(self, item):
        #O(N) runtime
        #O(1) space
        cur = self.head
        while(cur.next is not None):
            cur = cur.next
        cur.next = Node(item)
        self._size += 1
    
    def insertLasty(self, item):
      cur = head
      while cur.next is not None:
        cur = cur.next
      cur.next = Node(item)

    def removeBeginning(self):
        #O(1) runtime
        #O(1) space
        assert(self.size() > 0)
        #H -> 1 -> 2      remove()
        #H -> 2
        self.head.next = self.head.next.next
        self._size -= 1

    def removeBeg(self):
      self.head = self.head.next
      self._size -= 1
      return self.head

    def size(self):
        #O(1) runtime
        #O(1) space
        return self._size

    ## Own Coded

    def traverse(self, head):
      cur = head
      while cur is not None:
        cur = cur.next
        # do an action
      # return whatever
      return cur

    def removeEnd(self):
      cur = head
      while cur.next is not None:
        cur = cur.next
      cur.next = None      

    def reverse(self):
      cur = head
      prev = None
      # @QQQ why cur vs cur.next?
      for cur is not None:
        nexty = cur.next
        cur.next = prev

        prev = cur
        cur = cur.next
      # returning new head
      return prev

    def is_there_a_cycle(self):      
      slow = head
      fast = head
      # @QQQ NO wait of
      # while slow is not None:
      # while slow and fast:
      # @QQQ why is it not: "while fast.next"
      while fast and fast.next:
        # @QQQ diff between is and ==
        if slow is fast:
          return True
        slow = slow.next
        fast = fast.next.next
      return False

if __name__ == '__main__':
    #test cases
    linkedList = LinkedList()
    for i in range(1,6):
        linkedList.insertFront(i)
    #should print 5 | 4 | 3 | 2 | 1|
    print(linkedList)
    linkedList.removeBeginning()
    linkedList.removeBeginning()
    #should print 3,4,5
    print(linkedList)
    for i in range(6,11):
        linkedList.insertLast(i)
    #should print 3,4,5,6,7,8,9,10
    print(linkedList)
