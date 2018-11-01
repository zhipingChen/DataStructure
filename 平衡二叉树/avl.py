
# tree node definition
class Node(object):
    def __init__(self, value, height=0, lchild=None, rchild=None):
        self.lchild = lchild
        self.rchild = rchild
        self.value = value
        self.height = height

# tree definition
class Tree(object):
    def __init__(self, root=None):
        self.root = root

    # node in-order traversal(LDR)
    def traversal(self):
        traversal(self.root)

    # insert node
    def insert(self, value):
        self.root = insert(self.root, value)

    # delete node
    def delete(self, value):
        self.root = delete(self.root, value)

# node in-order traversal(LDR)
def traversal(node):
    if not node:
        return
    traversal(node.lchild)
    print(node.value, 'height=', node.height, end=', ')
    traversal(node.rchild)

# insert node
'''
the recursive insert operation has a flaw,
that the binary tree will recursively updates the height of the parent node 
even if the inserted element already exists.
'''
def insert(root, value):
    if not root:
        return Node(value)
    if value < root.value:
        root.lchild = insert(root.lchild, value)
    elif value > root.value:
        root.rchild = insert(root.rchild, value)
    return checkBalance(root)

# check whether the tree is balanced
def checkBalance(root):
    if not root:
        return None
    if abs(heightDiffL2R(root)) < 2:  # the tree is balance
        updateHeight(root)
    elif heightDiffL2R(root) == 2:  # situation L
        if heightDiffL2R(root.lchild) == -1:  # situation LR
            root.lchild = rotateR2L(root.lchild)
            root = rotateL2R(root)
        else:  # situation LL
            root = rotateL2R(root)
    elif heightDiffL2R(root) == -2:  # situation R
        if heightDiffL2R(root.rchild) == 1:  # situation RL
            root.rchild = rotateL2R(root.rchild)
            root = rotateR2L(root)
        else:  # situation RR
            root = rotateR2L(root)
    return root

# get the height difference between left-child and right-child
def heightDiffL2R(node):
    if node.lchild and node.rchild:
        return node.lchild.height - node.rchild.height
    if node.lchild:
        return node.lchild.height + 1
    if node.rchild:
        return -(node.rchild.height + 1)
    return 0

# update the height of the node
def updateHeight(root):
    if root.lchild and root.rchild:
        root.height = max(root.lchild.height, root.rchild.height) + 1
    elif root.lchild:
        root.height = root.lchild.height + 1
    elif root.rchild:
        root.height = root.rchild.height + 1
    else:
        root.height = 0

# rotate from left to right with the left-child node as the axis
def rotateL2R(node):
    leftChild = node.lchild
    leftChild.rchild, node.lchild = node, leftChild.rchild
    updateHeight(node)
    updateHeight(leftChild)
    return leftChild

# rotate from right to left with the right-child node as the axis
def rotateR2L(node):
    rightChild = node.rchild
    rightChild.lchild, node.rchild = node, rightChild.lchild
    updateHeight(node)
    updateHeight(rightChild)
    return rightChild

def delete(root, value):
    if not root:
        return None
    if root.value > value:
        root.lchild = delete(root.lchild, value)
    elif root.value < value:
        root.rchild = delete(root.rchild, value)
    else:
        if root.lchild and root.rchild:  # degree of the node is 2
            target = transferDeleteNode(root)
            root = delete(root, target)
            root.value = target
        else:  # degree of the node is [0|1]
            root = root.lchild if root.lchild else root.rchild
    return checkBalance(root)

# find the maximum node or the minimum node in the tree
def transferDeleteNode(node):
    if node.rchild.height > node.lchild.height:
        target = node.rchild
        while target.lchild:
            target = target.lchild
    else:
        target = node.lchild
        while target.rchild:
            target = target.rchild
    return target.value

if __name__ == '__main__':
    arr = [5, 3, 4, 0, 2, 1, 8, 6, 9, 7,7]
    T = Tree()
    for i in arr:
        T.insert(i)
    print('BST in-order traversal------------------')
    T.traversal()
    print('\ndelete test------------------')
    for i in arr[::-1]:
        print('after delete', i, end=',BST in-order is = ')
        T.delete(i)
        T.traversal()
        print()
