# tree node definition
class Node(object):
    def __init__(self, value, color = 'red', lchild = None, rchild = None, parent = None):
        self.lchild = lchild
        self.rchild = rchild
        self.parent = parent
        self.color = color
        self.value = value


# tree definition
class Tree(object):
    def __init__(self, root = None):
        self.root = root

    # node in-order traversal(LDR)
    def traversal(self):
        traversal(self.root)

    # insert node
    def insert(self, value):
        targetNode = findTargetNode(self.root, value)  # find the position
        if not targetNode:  # means the tree is none, case 1
            self.root = Node(value, color = 'black')
        else:
            node = insert(targetNode, value)  # insert the node
            adjustment(self, node) if node else None  # adjust the tree

    # delete node
    def delete(self, value):
        targetNode = findTargetNode(self.root, value)  # find the position
        if not targetNode:  # the value does not exist
            return
        if targetNode.lchild and targetNode.rchild:  # the node has two child nodes
            targetNode = transferDeleteNode(targetNode)
        delete(self, targetNode)


# node in-order traversal(LDR)
def traversal(node):
    if not node:
        return
    traversal(node.lchild)
    print(node.value, node.color, end = ' , ')
    traversal(node.rchild)


# find the right position according to value
def findTargetNode(node, value):
    target = node
    while node:
        if value < node.value:
            target, node = node, node.lchild
        elif value > node.value:
            target, node = node, node.rchild
        else:
            return node
    return target


# insert the child node
def insert(targetNode, value):
    if value < targetNode.value:
        targetNode.lchild = Node(value, parent = targetNode)
        return targetNode.lchild
    if value > targetNode.value:
        targetNode.rchild = Node(value, parent = targetNode)
        return targetNode.rchild


# change node color or rotate the subtree
def adjustment(tree, node):
    if not node.parent:  # case 1 : the node is the root node
        node.color = 'black'
    elif node.parent.color == 'black':  # case 2 : parent node is black
        pass
    else:  # parent node's color is red
        uncle = uncleNode(node)
        if uncle and uncle.color == 'red':  # case 3 : uncle node is red
            uncle.color, node.parent.color, uncle.parent.color = 'black', 'black', 'red'
            adjustment(tree, uncle.parent)
        else:  # uncle node does not exists or color is black
            rotationType, colorChange = rotationDetection(node)
            parent, grantParent = node.parent, node.parent.parent
            if colorChange: # case 4 : rotate and change color
                if rotationType == 'L2R':
                    node = rotateL2R(node.parent)
                elif rotationType == 'R2L':
                    node = rotateR2L(node.parent)
                parent.color,grantParent.color = 'black','red'
                if not node.parent:
                    tree.root = node
            else:  # case 5 : just rotate
                if rotationType == 'L2R':
                    node = rotateL2R(node).rchild
                elif rotationType == 'R2L':
                    node = rotateR2L(node).lchild
                adjustment(tree,node)



# get the uncle node
def uncleNode(node):
    grandParent = node.parent.parent
    return grandParent.rchild if node.parent == grandParent.lchild else grandParent.lchild


# confirm the rotation type is L2R or R2L, and whether needs to change the node color
def rotationDetection(node):
    parent, grandParent = node.parent, node.parent.parent
    if node == parent.lchild and parent == grandParent.lchild:
        return 'L2R', True
    if node == parent.rchild and parent == grandParent.rchild:
        return 'R2L', True
    if node == parent.lchild and parent == grandParent.rchild:
        return 'L2R', False
    if node == parent.rchild and parent == grandParent.lchild:
        return 'R2L', False


# rotate from left to right
def rotateL2R(node):
    parent, rchild = node.parent, node.rchild
    node.rchild, node.parent = parent, parent.parent  # regulate the node
    parent.parent, parent.lchild = node, rchild  # regulate the parent node
    if rchild:  # regulate the right child if not null
        rchild.parent = parent
    afterRotate(node, parent) # adjust the relationship between the node and it's new parent
    return node


# rotate from right to left
def rotateR2L(node):
    parent, lchild = node.parent, node.lchild
    node.lchild, node.parent = parent, parent.parent  # regulate the node
    parent.parent, parent.rchild = node, lchild  # regulate the parent node
    if lchild:  # regulate the left child if not null
        lchild.parent = parent
    afterRotate(node, parent) # adjust the relationship between the node and it's new parent
    return node

def afterRotate(node, parent):
    grantParent = node.parent
    if grantParent and parent == grantParent.lchild:
        grantParent.lchild = node
    elif grantParent and parent == grantParent.rchild:
        grantParent.rchild = node

# find the biggest node in the left subtree
def transferDeleteNode(node):
    target = node.lchild
    while target.rchild:
        target = target.rchild
    node.value, target.value = target.value, node.value
    return target


# balance the tree before delete the node
def balanceBeforeDelete(tree, node, parent):
    sibling = parent.rchild if node == parent.lchild else parent.lchild
    if sibling.color == 'black':
        siblingLeftChild, siblingRightChild = sibling.lchild, sibling.rchild
        if siblingRightChild and siblingRightChild.color == 'red':
            if node == parent.lchild:   # case 3.1 : right nephew is red
                newSubRoot, siblingRightChild.color = rotateR2L(sibling), 'black'
                if not newSubRoot.parent:
                    tree.root = newSubRoot
                elif parent.color == 'red':
                    parent.color, sibling.color = 'black', 'red'
            elif not siblingLeftChild or siblingLeftChild.color == 'black':   # case 3.2 : left nephew is red
                rotateR2L(siblingRightChild)
                siblingRightChild.color, sibling.color = 'black', 'red'
                balanceBeforeDelete(tree, node, parent)
        elif siblingLeftChild and siblingLeftChild.color == 'red':
            if node == parent.rchild:  # same as case 3.1
                newSubRoot, siblingLeftChild.color = rotateL2R(sibling), 'black'
                if not newSubRoot.parent:
                    tree.root = newSubRoot
                elif parent.color == 'red':
                    parent.color, sibling.color = 'black', 'red'
            elif not siblingRightChild or siblingRightChild.color == 'black': # same as case 3.2
                rotateL2R(siblingLeftChild)
                siblingLeftChild.color, sibling.color = 'black', 'red'
                balanceBeforeDelete(tree, node, parent)
        elif parent.color == 'black':             # case 3.3 : parent is black
            sibling.color = 'red'
            if parent.parent:  # parent is not the root node
                balanceBeforeDelete(tree, parent, parent.parent)
        else:                                    # case 3.4 : parent is red
            parent.color, sibling.color = 'black', 'red'
    else:                                 # case 3.5 : sibling is red
        if node == parent.lchild:
            newSubRoot, parent.color, sibling.color = rotateR2L(sibling), 'red', 'black'
        else:
            newSubRoot, parent.color, sibling.color = rotateL2R(sibling), 'red', 'black'
        if not newSubRoot.parent:
            tree.root = newSubRoot
        balanceBeforeDelete(tree, node, parent)


# delete node
def delete(tree, node):
    if node.color == 'red':  # case 1 : the node color is red
        if node == node.parent.lchild:
            node.parent.lchild = None
        else:
            node.parent.rchild = None
    else:
        parent, child = node.parent, node.lchild if node.lchild else node.rchild
        if not parent:  # the node is the root node
            tree.root = child
        if child:   # case 2 : the node is black with one red child
            if parent: # the node is not the root node
                if node == parent.lchild:
                    parent.lchild = child
                else:
                    parent.rchild = child
            child.color, child.parent = 'black', parent
        else: # case 3 : the node is black with no child
            if parent: # the node is not the root node
                balanceBeforeDelete(tree, node, parent)
                if node == parent.lchild:
                    parent.lchild = None
                else:
                    parent.rchild = None

if __name__ == '__main__':
    arr = [5, 3, 4, 0, 2, 1, 8, 6, 9, 7]
    T = Tree()
    print('\ninsert test------------------')
    for i in arr:
        print('after insert', i, end = ',BST in-order is = ')
        T.insert(i)
        T.traversal()
        print()

    print('\ndelete test------------------')
    for i in arr:
        print('after delete', i, end = ',BST in-order is = ')
        T.delete(i)
        T.traversal()
        print()