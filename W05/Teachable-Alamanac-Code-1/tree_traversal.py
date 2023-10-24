from BST import BinarySearchTree
#prints out nodes in sorted order
def inorder(root,arr):
    if root is None:
        return
    inorder(root.left,arr)
    arr.append(root.val)
    inorder(root.right,arr)

#prints out nodes in reverse sorted order
def reverse_inorder(root, arr):
    if root is None:
        return
    reverse_inorder(root.right,arr)
    arr.append(root.val)
    reverse_inorder(root.left, arr)

#10,6,2,4,3,5,7,15,12,20

   #                 10
   #     6               15
   # 2       7       12       20
   #   4
   #  3 5

#out - [10,6,2,4,3,5,7,15,12,20]

def preorder(root,arr):
    if root is None:
        return
    arr.append(root.val)
    preorder(root.left, arr)
    preorder(root.right,arr)



def postorder(root,arr):
    if root is None:
        return
    postorder(root.left, arr)
    postorder(root.right,arr)
    arr.append(root.val)






if __name__ == '__main__':
    # initialize tree
    BST = BinarySearchTree()
    BST.put(10,10)
    BST.put(6,6)
    BST.put(15,15)
    BST.put(20,20)
    BST.put(12,12)
    BST.put(7,7)
    BST.put(2,2)
    BST.put(4,4)
    BST.put(5,5)
    BST.put(3,3)
    print(BST)
    arr = []
    inorder(BST.root, arr)
    print("inorder:")
    print(arr)
    arr = []
    reverse_inorder(BST.root, arr)
    print("reverse inorder:")
    print(arr)
    #inorder - [2,3,4,5,6,7,10,15,20]
    #reverse_inorder [20,15,10,7,5,2]
    arr = []
    preorder(BST.root, arr)
    print("preorder:")
    print(arr)
    arr = []
    postorder(BST.root, arr)
    print("postorder:")
    print(arr)




    #go all the way left
    # BST = BinarySearchTree()
    # BST.put(10,10)
    # BST.put(11,11)
    # BST.put(1,1)
    # BST.put(2,2)
    # BST.put(3,3)
    # BST.put(4,4)
    # BST.put(5,5)
    # BST.put(6,6)
    # BST.put(7,7)
    # BST.put(8,8)
    # BST.put(9,9)
    # BST.put(12,12)
    # BST.put(13,13)
    # BST.put(14,14)
    # BST.put(15,15)
    # BST.put(16,16)
    # BST.put(17,17)
    # print(BST)
    # arr = []
    # inorder(BST.root, arr)
    # print("inorder:")
    # print(arr)
    # arr = []
    # reverse_inorder(BST.root, arr)
    # print("reverse inorder:")
    # print(arr)
    # #inorder - [2,3,4,5,6,7,10,15,20]
    # #reverse_inorder [20,15,10,7,5,2]
    # arr = []
    # preorder(BST.root, arr)
    # print("preorder:")
    # print(arr)
    # arr = []
    # postorder(BST.root, arr)
    # print("postorder:")
    # print(arr)
