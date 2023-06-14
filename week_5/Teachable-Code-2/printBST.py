def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

def recursive_append(node,cur_height,lo,hi,output):
    if node is None:
        return
    mid = (lo + hi)//2
    output[cur_height][mid] = str(node.val)
    recursive_append(node.left,cur_height+1,lo,mid-1,output)
    recursive_append(node.right,cur_height+1,mid+1,hi,output)


def binaryTreeToStr(root):
    """
    :type root: TreeNode
    :rtype: List[List[str]]
    """
    tree_height = height(root)
    length = 2**tree_height-1
    output = [[" " for x in range(length)] for x in range(tree_height)]
    recursive_append(root,0,0,length-1,output)
    str_out = ""
    for row in output:
        for c in row:
            str_out += c
        str_out += "\n"
    return str_out
