from printBST import binaryTreeToStr
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#     5
#   3   7
#  2 4 6 8

#    5
#  3
#   4
#


#     None

class BST:
    def __init__(self):
        self.root = None

    #prints our BST in string format
    def __str__(self):
        return binaryTreeToStr(self.root)

    def insertIterative(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            prev = None
            isLeft = None
            cur = self.root
            while(cur):
                prev = cur
                if cur.val > val:
                    isLeft = True
                    cur = cur.left
                else:
                    isLeft = False
                    cur = cur.right
            if isLeft:
                prev.left = Node(val)
            else:
                prev.right = Node(val)


    def insertRecursive(self, val):
        self.root = self._insertRecursive(val, self.root)

    def _insertRecursive(self, val, curNode):
        if not curNode:
            return Node(val)
        if curNode.val > val:
            curNode.left = self._insertRecursive(val, curNode.left)
        else:
            curNode.right = self._insertRecursive(val, curNode.right)
        return curNode


if __name__ == '__main__':
    #test cases
    bst = BST()
    bst.insertIterative(5)
    bst.insertIterative(3)
    bst.insertIterative(7)
    bst.insertIterative(2)
    bst.insertIterative(4)
    bst.insertIterative(6)
    bst.insertIterative(8)
    print(bst)

    bst = BST()
    bst.insertRecursive(5)
    bst.insertRecursive(3)
    bst.insertRecursive(7)
    bst.insertRecursive(2)
    bst.insertRecursive(4)
    bst.insertRecursive(6)
    bst.insertRecursive(8)
    print(bst)
