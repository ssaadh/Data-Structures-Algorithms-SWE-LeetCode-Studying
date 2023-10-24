from printBST import binaryTreeToStr
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    #prints our BST in string format
    def __str__(self):
        return binaryTreeToStr(self.root)

    #return true if value exists in BST
    def getIterative(self, val):
        cur = self.root
        while(cur):
            if cur.val == val:
                return True
            elif cur.val > val:
                cur = cur.left
            else:
                cur = cur.right
        return False

    def getRecursive(self, val):
        return self._getRecursive(val, self.root)

    def _getRecursive(self, val, curNode):
        if not curNode:
            return False
        if curNode.val == val:
            return True
        elif curNode.val > val:
            return self._getRecursive(val, curNode.left)
        else:
            return self._getRecursive(val, curNode.right)




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
    def makeTree():
        bst = BST()
        bst.insertRecursive(5)
        bst.insertRecursive(3)
        bst.insertRecursive(4)
        bst.insertRecursive(7)
        bst.insertRecursive(2)
        bst.insertRecursive(6)
        bst.insertRecursive(8)
        return bst
    bst = makeTree()
    print(bst)
    # for i in range(10):
    #     print(i, bst.getIterative(i), bst.getRecursive(i))
