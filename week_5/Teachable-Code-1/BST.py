from printBST import PrintBST

class leafNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return PrintBST().printTree(self.root)

    #adds item to tree
    def put(self, key, val):
        self.root = self._put(key, val, self.root)

    def _put(self, key, val, node):
        if node is None:
            return leafNode(key, val)
        if node.key == key:
            node.val = val
        elif node.key > key:
            node.left = self._put(key, val, node.left)
        else:
            node.right = self._put(key, val, node.right)
        return node

    #if key exists then return that keys value
    def get(self, key):
        return self._get(key, self.root)

    def _get(self, key, node):
        if node is None:
            return None
        if node.key == key:
            return node.val
        if node.key > key:
            return self._get(key, node.left)
        else:
            return self._get(key, node.right)

    #if key exists delete key and value
    def delete(self, key):
        self.root = self._delete(key, self.root)

    def _delete(self, key, node):
        #case 1 - cant find key then we do nothing
        if node is None:
            return
        if node.key > key:
            node.left = self._delete(key, node.left)
        elif node.key < key:
            node.right = self._delete(key, node.right)
        else:
        #case 2 - we find the key and it has no children
            if node.left is None and node.right is None:
                return None

            elif node.left and node.right:
                #case 4 - 2 children
                temp = node
                cur = node.right
                while(cur.left):
                    cur = cur.left
                self._delete(cur.key, temp.right)
                cur.left = temp.left
                cur.right = temp.right
                return cur
            else:
                #case 3 - we find the key and it has one child
                if node.right:
                    return node.right
                else:
                    return node.left
        return node

if __name__ == '__main__':
    #test cases
    bst = BinarySearchTree()
    bst.put(3,3)
    bst.put(2,2)
    bst.put(4,4)
    print(bst)
    print(bst.get(4))
    print('\n')
    bst.delete(4)
    print(bst)
    print("\n")
    bst.delete(3)
    print(bst)
    print("\n")
    bst.delete(2)
    bst.put(1,1)
    bst.put(2,2)
    bst.put(3,3)
    bst.put(4,4)
    bst.put(5,5)
    print(bst)
