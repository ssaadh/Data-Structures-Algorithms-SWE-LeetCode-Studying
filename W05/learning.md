level
D B F A C E G
in order
A B C D E F G
pre
D B A C F E G
post
A C B E G F D

We say that the depth of a node is the number of edges between it and the root of the tree. Node C above has a depth of 2 since there are two edges between D (the root)  and C.

The height of a binary tree is the number of edges between the root and the node of maximum depth

A binary search tree is complete if it is completely filled in. This means that every node except the bottom-most level has 2 children.

A binary search tree is balanced if the height of every leaf node differs by at most 1.

A BST is a binary tree with the following properites:
- All keys in the left subtree are less than the key in the parent node.
- All keys in the right subtree are greater than the key in the parent node.
- There are no duplicate keys
- Both the left and right subtrees must also be binary search trees. 
