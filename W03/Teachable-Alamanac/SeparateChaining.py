class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None

class SeparateChainingHashMap:
    #initializes HashMap
    def __init__(self, capacity):
        #O(capacity) rt
        #O(capacity) space
        self.map = [Node("dummy", "dummy") for _ in range(capacity)]

    #returns index that key is stored
    def hashedIndex(self, key):
        #O(1) O(1)
        return key % len(self.map)

    #adds an item to the hash map. uses separate chaining for collisions
    def put(self, key, val):
        #O(N)/capacity RT
        #O(1) space
        idx = self.hashedIndex(key)
        cur = self.map[idx]
        while(cur.next):
            if cur.next.key == key:
                cur.next.val = val
                return
            cur = cur.next
        cur.next = Node(key,val)

    #finds item with given key and returns associated val
    def get(self, key):
                #O(N)/capacity RT
                #O(1) space
        idx = self.hashedIndex(key)
        cur = self.map[idx]
        while(cur.next):
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next

    #deletes a key and its val from the hashmap
    def delete(self, key):
        idx = self.hashedIndex(key)
        prev = self.map[idx]
        cur = prev.next
        while(cur):
            if cur.key == key:
                prev.next = cur.next
            prev = cur
            cur = cur.next


    #overrides toString method for debugging
    def __str__(self):
        #O(N)
        #O(N)
        out = ""
        for idx in range(len(self.map)):
            cur = self.map[idx].next
            while(cur):
                out += str(cur.val) + " "
                cur = cur.next
            out += "\n"
        return out


if __name__ == '__main__':
    #test cases
    map = SeparateChainingHashMap(3)
    for i in range(10):
        map.put(i,i*2)
    #0 6
    #2 8
    #4
    print(map)
    print(map.get(4))
    for i in range(3):
        map.delete(i)
    print(map)
