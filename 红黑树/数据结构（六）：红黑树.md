![](http://upload-images.jianshu.io/upload_images/9738807-a31a5c6cc16432f9.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1080/q/50)




红黑树是一种自平衡二叉查找树，与 AVL 树类似，提供 $O(log N)$ 级别的查询、插入和删除节点复杂度。相对于 AVL 树单纯的对每个节点的平衡因子进行判断，红黑树给节点赋予了颜色属性，并通过对树中节点的颜色进行限制，来保持整棵树的平衡。

> 之前提到的自平衡二叉查找树，即 AVL 树，属于一种高度平衡的二叉查找树，对每个节点的平衡因子进行严苛的限制，所以 AVL 树能够提供 $O(log N)$ 的节点查询复杂度。也因为对每个节点的平衡因子限制较大，所以插入和删除节点时，需要进行很频繁的平衡调节操作。
\
红黑树相对于 AVL 树，对树的高度限制较为宽松，所以红黑树的查找复杂度要略逊于 AVL 树。也因为对树高度的限制较小，所以插入和删除节点时需要较少的旋转操作即可达到平衡状态。

### 条件限制

红黑树中的节点存在颜色属性，通过对节点颜色的限制来保持树的平衡性。平衡的红黑树要求如下：
1. 节点是红色或者黑色；
2. 根节点是黑色；
3. 叶子节点是黑色；
4. 红色节点必须具有两个黑色子节点；
5. 从任一节点到其后代的叶子节点路径中包含相同个数的黑色节点。

> 其中 1、2 条没什么可说的，第 3 条中提到叶子节点，在红黑树的使用过程中使用一个特殊的节点 $Nil$ 来表示叶子节点，该节点代表着终结条件，在算法导论中称这种使用方式为哨兵模式。在后续的 python 代码中以 $None$ 来代表该终结条件。
\
第四条所要描述的内容，就是两个红色节点不能以父子关系相邻。
\
因为黑色节点之间可以穿插着红色节点，所以第五条保证了任一子二叉树中，从根节点到叶子节点的最长路径不多于最短路径的二倍。

***note***：后续的示例中隐藏叶子节点 $Nil$ 的表示，所以看到红色叶子节点属于正常情况

### 插入节点情况

> 待插入新节点颜色初始为红色，因为红色节点的插入不一定影响红黑树的平衡性，而黑色节点的插入一定会引起红黑树的不平衡。

**新节点的插入有如下几种情形：**

**1 新节点为根节点。**
> 即当前红黑树为空树，插入新节点后，只需要变换节点颜色为黑色，即可满足红黑树的平衡限制条件；

![original](https://upload-images.jianshu.io/upload_images/9738807-abe5e3f3cf51e965.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)     |       ![adjusted](https://upload-images.jianshu.io/upload_images/9738807-264dbef233d725ae.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)            
--------------------|:-----------------------------------:
**2. 新节点的父节点为黑色。**
> 若新节点不为根节点，则具有父节点，父节点颜色无外乎黑、红两种。当父节点颜色为黑色时，此时插入新节点不影响红黑树的平衡性，所以不需要调整操作；

**3. 新节点的父节点为红色，同时叔父节点的颜色也为红色。**
> 若父节点和叔父节点的颜色都为红色，则根据条件 4 ，祖父节点的颜色为黑色。因为新插入节点颜色为红色，违反了条件 4，此时只需要变换父节点和叔父节点的颜色为黑色，祖父节点的颜色为红色即可。变换颜色后，只需要考虑祖父节点颜色为红色，是否违反了条件限制，将祖父节点作为“新”节点，递归进行处理即可。

![original](https://upload-images.jianshu.io/upload_images/9738807-caff6b7b7389d919.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)    |     ![adjusted](https://upload-images.jianshu.io/upload_images/9738807-e11b5f462fecf5b6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
--------------------|:-----------------------------------:

> 此时无所谓新节点是其父节点的左子节点或右子节点。

**4. 新节点的父节点为红色，叔父节点的颜色不为红色。且新节点 $N$ 是其父节点 $P$ 的左子节点，同时父节点 $P$ 是祖父节点 $G$ 的左子节点；或者新节点 $N$ 是其父节点 $P$ 的右子节点，同时父节点 $P$ 是祖父节点 $G$ 的右子节点。**

> 不妨假设新节点 $N$ 是其父节点 $P$ 的左子节点，同时父节点 $P$ 是祖父节点 $G$ 的左子节点。因为父节点 $P$ 为红色，所以祖父节点 $G$ 颜色为黑色。此时以 $P$ 节点为轴心执行一次右旋操作，并对父节点 $P$ 和祖父节点 $G$ 进行颜色变换。

![original](https://upload-images.jianshu.io/upload_images/9738807-1e1bc2bfb5cc9279.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)    |     ![adjusted](https://upload-images.jianshu.io/upload_images/9738807-2abc65b3500d24ed.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
--------------------|:-----------------------------------:

> 旋转后的变色操作，保证了通过每个节点到后代叶子节点的路径上，包含的黑色节点个数不变，即满足了条件约束。

> 新节点 $N$ 不一定只是一个单一的新插入节点，也可能是一颗二叉树的根节点，例如情形 3 的处理后，递归处理的“新”节点就是二叉树的根节点。空白的部分表示此处可能为空树或非空树，其实这里的叔父节点 $U$ 也可以是空树或非空树。

**5. 新节点的父节点为红色，叔父节点的颜色不为红色。且新节点 $N$ 是其父节点 $P$ 的右子节点，同时父节点 $P$ 是祖父节点 $G$ 的左子节点；或者新节点 $N$ 是其父节点 $P$ 的左子节点，同时父节点 $P$ 是祖父节点 $G$ 的右子节点。**

> 不妨假设新节点 $N$ 是其父节点 $P$ 的右子节点，同时父节点 $P$ 是祖父节点 $G$ 的左子节点。因为父节点 $P$ 为红色，所以祖父节点 $G$ 颜色为黑色。此时以节点 $N$ 为轴心执行一次左旋操作。

![d1.png](https://upload-images.jianshu.io/upload_images/9738807-295922ccaad63f96.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)    |    ![d1.png](https://upload-images.jianshu.io/upload_images/9738807-09a83555b7ca2a6b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
--------------------|:-----------------------------------:

> 旋转操作前后，通过每个节点到后代叶子节点的路径上，所经过的黑色节点个数不发生变化。此时情形转变为情形 4，所以按照情形 4 进行处理即可。

> 由插入节点的情形分析可知，插入节点时最多只会进行两次旋转操作，即情形 5 旋转后变为情形 4，情形 4 旋转变色后满足平衡条件。变色操作则可能递归进行到根节点。

### 节点插入后调整代码
```
def adjustment(tree, node):
    if not node.parent:                        # case 1 : the node is the root node
        node.color = 'black'
    elif node.parent.color == 'black':         # case 2 : parent node is black
        pass
    else:  # parent node's color is red
        uncle = uncleNode(node)
        if uncle and uncle.color == 'red':      # case 3 : uncle node is red
            uncle.color, node.parent.color, uncle.parent.color = 'black', 'black', 'red'
            adjustment(tree, uncle.parent)
        else:  # uncle node does not exists or color is black
            rotationType, colorChange = rotationDetection(node)
            parent, grantParent = node.parent, node.parent.parent
            if colorChange:                       # case 4 : rotate and change color
                if rotationType == 'L2R':
                    node = rotateL2R(node.parent)
                elif rotationType == 'R2L':
                    node = rotateR2L(node.parent)
                parent.color,grantParent.color = 'black','red'
                if not node.parent:
                    tree.root = node
            else:                                   # case 5 : just rotate
                if rotationType == 'L2R':
                    node = rotateL2R(node).rchild
                elif rotationType == 'R2L':
                    node = rotateR2L(node).lchild
                adjustment(tree,node)
```

### 删除节点情况

> 二叉查找树在进行节点删除时，若待删除节点的度为 2 时，则可以将删除操作“转移”到其后代度不为 2 的子节点上，所以后续讨论的待删除节点的度都不为 2。

**节点删除有如下几种情形：**

**1. 待删除节点颜色为红色。**

> 因为待删除节点的度为 0 或 1，根据条件 5 可知，该待删除节点为叶子节点，所以直接删除该节点并不影响二叉树的平衡性。

**2. 待删除节点为黑色，度为 1。**

> 根据条件 5 可知，若待删除节点度为 1，则子节点颜色为红色。此时可以直接删除该节点，用子节点来填充该节点位置，对子节点进行颜色变换即可。

**3. 待删除节点为黑色，度为 0。**

> 情形 1, 2 中的节点删除场景较为简单，可以直接进行节点删除操作，最多只需要通过节点颜色变换即可保持二叉树的平衡性（注意根节点的变化）。若待删除节点度为 0，此时不妨对二叉树先进行一番预平衡操作，然后再进行节点删除，以此保证删除节点后二叉树处于平衡状态。

### 简单场景下节点删除代码
```
def delete(tree, node):
    if node.color == 'red':               # case 1 : the node color is red
        if node == node.parent.lchild:
            node.parent.lchild = None
        else:
            node.parent.rchild = None
    else:
        parent, child = node.parent, node.lchild if node.lchild else node.rchild
        if not parent:   # the node is the root node
            tree.root = child
        if child:                        # case 2 : the node is black with one red child
            if parent: # the node is not the root node
                if node == parent.lchild:
                    parent.lchild = child
                else:
                    parent.rchild = child
            child.color, child.parent = 'black', parent
        else:                          # case 3 : the node is black with no child
            if parent: # the node is not the root node
                balanceBeforeDelete(tree, node, parent)
                if node == parent.lchild:
                    parent.lchild = None
                else:
                    parent.rchild = None
```

> 下面以 $N$ 表示待删除节点，以 $P$ 表示待删除节点的父节点，以 $S$ 表示待删除节点的兄弟节点，以 $S_l$ 表示兄弟节点的左子节点，以 $S_r$ 表示兄弟节点的右子节点。不妨以 $N$ 节点作为 $P$ 节点的左子节点进行讨论，对称的情况下处理过程类似。

**3.1 兄弟节点 $S$ 为黑色，$S_r$ 节点为红色。**

> 兄弟节点 $S$ 的右子节点 $S_r$  为红色，则兄弟节点 $S$  为黑色，父节点 $P$ 颜色不确定。此时以节点 $S$ 为轴心执行左旋操作，并对部分节点执行颜色变换操作。

![original](https://upload-images.jianshu.io/upload_images/9738807-3fad871f33a53d62.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)    |    ![adjusted](https://upload-images.jianshu.io/upload_images/9738807-1a88bae5af0387c7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
--------------------|:-----------------------------------:

> 左旋操作后，变换 $S_r$ 节点颜色。若 $P$ 节点为红色，则左旋操作后，对 $P$ 节点和 $S$ 节点进行颜色变换。此时删除节点 $N$ 之后，通过其他节点的路径上黑色节点个数不变，满足平衡条件。

**3.2 兄弟节点 $S$ 为黑色，$S_l$ 节点为红色，$S_r$ 节点不为红色。**

> 兄弟节点 $S$ 的左子节点 $S_r$  为红色，则兄弟节点 $S$  为黑色，父节点 $P$ 颜色不确定，$S_r$ 节点不存在或存在为黑色。此时以节点 $S_l$ 为轴心执行右旋操作，并对 $S$ 和 $S_l$ 节点执行颜色变换操作。

![original](https://upload-images.jianshu.io/upload_images/9738807-c6ad0ab56fec42b7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)    |    ![adjusted](https://upload-images.jianshu.io/upload_images/9738807-9a3a3748e14d7b08.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
--------------------|:-----------------------------------:

> 执行右旋操作后可以发现，此时情形演变为情形 3.1，所以此时再次对待删除节点 $N$ 进行平衡操作即可。

**3.3 兄弟节点 $S$ 为黑色，$S$ 节点没有红色子节点，且父节点 $P$ 为黑色。**

> 兄弟节点 $S$ 和父节点 $P$ 为黑色，且兄弟节点 $S$ 没有红色子节点，此时对 $S$ 进行颜色变换。

![original](https://upload-images.jianshu.io/upload_images/9738807-9e516f3702841acc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)   |   ![adjusted](https://upload-images.jianshu.io/upload_images/9738807-41c22e3eee2749bb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
--------------------|:-----------------------------------:

> 对兄弟节点 $S$ 进行颜色变换后，可以发现，忽略待删除节点 $N$，此时父节点 $P$ 处于和待删除节点 $N$ 同样的处境，即通过该节点的路径上黑色节点个数减一。所以此时将父节点 $P$ 作为新的节点 $N$ 进行同样的预平衡操作。

**3.4 兄弟节点 $S$ 为黑色，$S$ 节点没有红色子节点，且父节点 $P$ 为红色。**

> 兄弟节点 $S$ 为黑色，且没有红色子节点，父节点 $P$ 为红色，此时只需要对节点 $S$ 和 $P$ 进行颜色变换即可。

![original](https://upload-images.jianshu.io/upload_images/9738807-ae20638c892e15a6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)   |   ![adjusted](https://upload-images.jianshu.io/upload_images/9738807-41c22e3eee2749bb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
--------------------|:-----------------------------------:

> 对兄弟节点 $S$ 和父节点 $P$ 进行颜色变换后，可以发现，忽略待删除节点 $N$，此时通过各节点的路径上黑色节点个数不变，即二叉树处于平衡状态。

**3.5 兄弟节点 $S$ 为红色。**

> 兄弟节点 $S$ 为红色，则此时父节点 $P$ 为黑色。此时以 $S$ 节点为轴心进行左旋操作，并对节点 $S$ 和 $P$ 进行变色操作。

![original](https://upload-images.jianshu.io/upload_images/9738807-107d9f5aed175d3e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  |  ![adjusted](https://upload-images.jianshu.io/upload_images/9738807-2c02c46ec515c061.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
--------------------|:-----------------------------------:

> 旋转并进行节点颜色变换后，可以发现，此时的二叉树同样处于平衡状态，所以这一步的旋转与颜色变换操作只是一个过渡处理，并没有起到预平衡的作用，即删除节点 $N$ 之后，二叉树仍然是不平衡的。但是经过该步的处理之后，二叉树的状态演变为情形 3.1，3.2 或者 3.4 中的一种，所以可以对待删除节点 $N$ 再次进行预平衡处理。

> 节点删除的所有情况如上，由各个情形描述可知，节点删除最多经过三次旋转即可达到平衡状态，即情形 3.5 旋转后变为情形 3.2，情形 3.2 旋转后变为情形 3.1，情形 3.1 旋转后满足平衡条件。变色操作则可能递归进行到根节点。

### 预平衡代码
```
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
```

### 总结

红黑树的非严格平衡结构使得其查询性能要略高于 AVL 树，同样因为对高度平衡的要求较低，所以删除和插入节点性能要高于 AVL 树。其中插入节点和删除节点需要分为多个情况进行讨论，插入新节点最多需要两次旋转操作即可达到平衡状态，删除节点最多三次旋转即可恢复平衡。

> 附上一个数据结构可视化网站，可以更直观的观察各种数据结构的调整过程：https://www.cs.usfca.edu/~galles/visualization/Algorithms.html

### 代码附录
```
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
```
### 测试代码及输出
```
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
```
输出为：
```
insert test------------------
after insert 5,BST in-order is = 5 black , 
after insert 3,BST in-order is = 3 red , 5 black , 
after insert 4,BST in-order is = 3 red , 4 black , 5 red , 
after insert 0,BST in-order is = 0 red , 3 black , 4 black , 5 black , 
after insert 2,BST in-order is = 0 red , 2 black , 3 red , 4 black , 5 black , 
after insert 1,BST in-order is = 0 black , 1 red , 2 red , 3 black , 4 black , 5 black , 
after insert 8,BST in-order is = 0 black , 1 red , 2 red , 3 black , 4 black , 5 black , 8 red , 
after insert 6,BST in-order is = 0 black , 1 red , 2 red , 3 black , 4 black , 5 red , 6 black , 8 red , 
after insert 9,BST in-order is = 0 black , 1 red , 2 red , 3 black , 4 black , 5 black , 6 red , 8 black , 9 red , 
after insert 7,BST in-order is = 0 black , 1 red , 2 red , 3 black , 4 black , 5 black , 6 red , 7 red , 8 black , 9 red , 

delete test------------------
after delete 5,BST in-order is = 0 black , 1 red , 2 red , 3 black , 4 black , 6 black , 7 red , 8 red , 9 black , 
after delete 3,BST in-order is = 0 black , 1 red , 2 black , 4 black , 6 black , 7 red , 8 red , 9 black , 
after delete 4,BST in-order is = 0 red , 1 black , 2 black , 6 black , 7 red , 8 red , 9 black , 
after delete 0,BST in-order is = 1 black , 2 black , 6 black , 7 red , 8 red , 9 black , 
after delete 2,BST in-order is = 1 black , 6 red , 7 black , 8 black , 9 black , 
after delete 1,BST in-order is = 6 black , 7 red , 8 black , 9 black , 
after delete 8,BST in-order is = 6 black , 7 black , 9 black , 
after delete 6,BST in-order is = 7 black , 9 red , 
after delete 9,BST in-order is = 7 black , 
after delete 7,BST in-order is = 
```
