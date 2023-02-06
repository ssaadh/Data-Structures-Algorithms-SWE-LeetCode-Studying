class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    # creates an empty Stack
    def __init__(self):
        #O(1) time and space
        self.first_item = None
        self._size = 0

    #prints out stack in order
    def __str__(self):
        #4->3->2->1
        #O(N) time and space
        cur = self.first_item
        out = ""
        while(cur):
            out += str(cur.val)+"|"
            cur = cur.next
        return out

    # adds an item to the stack
    def push(self, item):
        #add 5
        #5 -> 4 -> 3 -> 2
        #O(1) time and space
        old_first_item = self.first_item
        self.first_item = Node(item)
        self.first_item.next = old_first_item
        self._size += 1


    # removes and returns the most recently added item
    def pop(self):
        #O(1) time and space
        if self.isEmpty():
            return

        #4->3->2
        #3->2

        old_first_item = self.first_item
        self.first_item = self.first_item.next
        self._size -= 1
        return old_first_item.val


    # Returns a boolean indicating if the stack is empty
    def isEmpty(self):
        return self.size() == 0

    # returns the number of items in the stack
    def size(self):
        return self._size

if __name__ == '__main__':
    #test cases
    stack = Stack()
    for i in range(5):
        stack.push(i)
    #4,3,2,1,0
    print(stack)

    for _ in range(3):
        #should print 4,3,2,1,0
        print(stack.pop())

    for i in range(5,10):
        stack.push(i)
    #9,8..5, 1,0
    print(stack)
