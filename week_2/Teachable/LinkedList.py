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

    def insertLast(self, item):
        #O(N) runtime
        #O(1) space
        cur = self.head
        while(cur.next is not None):
            cur = cur.next
        cur.next = Node(item)
        self._size += 1

    def removeBeginning(self):
        #O(1) runtime
        #O(1) space
        assert(self.size() > 0)
        #H -> 1 -> 2      remove()
        #H -> 2
        self.head.next = self.head.next.next
        self._size -= 1

    def size(self):
        #O(1) runtime
        #O(1) space
        return self._size

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
