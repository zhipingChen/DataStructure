![](https://upload-images.jianshu.io/upload_images/9738807-4b563043fd581181.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> 通过之前对[二叉搜索树](https://www.jianshu.com/p/ff4b93b088eb)介绍可知，将集合构造为二叉搜索树结构，该结构下对树中节点的查询、删除和插入三种操作，时间复杂度均为 $O(log_2N)$~$O(N)$。影响时间复杂度的因素即为二叉树的高，为了尽量避免树中每层上只有一个节点的情况，这里引入平衡二叉树。

### 定义

平衡二叉树也叫自平衡二叉搜索树（Self-Balancing Binary Search Tree），所以其本质也是一颗二叉搜索树，不过为了限制左右子树的高度差，避免出现倾斜树等偏向于线性结构演化的情况，所以对二叉搜索树中每个节点的左右子树作了限制，左右子树的高度差称之为平衡因子，树中每个节点的平衡因子绝对值不大于 $1$，此时二叉搜索树称之为平衡二叉树。

自平衡是指，在对平衡二叉树执行插入或删除节点操作后，可能会导致树中某个节点的平衡因子绝对值超过 $1$，即平衡二叉树变得“不平衡”，为了恢复该节点左右子树的平衡，此时需要对节点执行旋转操作。

### 情景分析

在执行插入或删除节点操作后，平衡因子绝对值变为大于 $1$ 的情况，即左右子树的高度差为 $-2$ 或 $2$ 的情况，可以归纳为如下四种：

* **左左情况(LL)**

$LL$ 情况是指根节点的平衡因子为 $2$，根节点的左子节点平衡因子为 $0$ 或 $1$ 。

![LL_1](https://upload-images.jianshu.io/upload_images/9738807-7887d5d201f0e9b3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

如图 ***LL_1*** 所示，当节点 $C$ 的子节点被删除，或者节点 $D$ 插入子节点 $F$ 时，根节点 $A$ 的平衡因子变为 $2$，$A$ 的左子节点 $B$ 的平衡因子为 $1$。

![LL_2](https://upload-images.jianshu.io/upload_images/9738807-ddc2fd5055daafbd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

或者如图 ***LL_2*** 所示，当节点 $C$ 的子节点被删除，根节点 $A$ 的平衡因子变为 $2$，$A$ 的左子节点 $B$ 的平衡因子为 $0$。

> 当根节点的左子树高度比右子树的高度大 $2$，因为平衡二叉树是一种有序结构，节点值之间具有大小关系，所以如果根节点保持不变，左右子树始终分隔两岸，则无论如何调整节点位置，二叉树始终不可能恢复平衡。所以需要更换根节点，使得新的根节点的左右子树的高度趋于平衡。

该情况下需要对平衡二叉树执行右旋操作：
1. 设置根节点 $root$ 的左子节点为新的根节点 $root_{new}$；
2. 将 $root_{new}$ 节点的右子树作为 $root$ 节点的左子树，将  $root$ 节点作为 $root_{new}$ 的右子树，即降低“左子树”高度，提升“右子树”高度，使得新的左右子树高度趋于平衡；

对于图 ***LL_1***，节点 $B$ 的平衡因子为 $1$，设 $B$ 节点的左子树 $D$ 高度为 $h$，则右子树 $E$ 高度为$h-1$，因为 $A$ 的平衡因子为 $2$，所以二叉树 $C$ 的高度为： $h-1$。则右旋操作后，$B$ 的左子树高度不变为 $h$，右子树高度为：$1+max(height(C),height(E))=h$，此时二叉树为平衡二叉树，如下图 ***balanced_LL_1***。

![balanced_LL_1](https://upload-images.jianshu.io/upload_images/9738807-2d3a1dd4b02ffed1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

对于图 ***LL_2***，节点 $B$ 的平衡因子为 $0$，设 $B$ 节点的左右子树高度为 $h$，则二叉树 $C$ 的高度为： $h-1$。右旋操作后，$B$ 的左子树高度不变为 $h$，右子树高度为：$1+max(height(C),height(E))=h+1$，此时二叉树为平衡二叉树，如下图 ***balanced_LL_2***。

![balanced_LL_2](https://upload-images.jianshu.io/upload_images/9738807-ea0f758bc870e4f3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

##### 右旋代码
```
# rotate from left to right with the left-child node as the axis
def rotateL2R(node):
    leftChild = node.lchild
    leftChild.rchild,node.lchild = node,leftChild.rchild   # rotate
    updateHeight(node)
    updateHeight(leftChild)
    return leftChild
```

其中 $updateHeight$ 函数作用为更新调整后节点的平衡因子，因为右旋操作平衡因子变化的节点只有两个：原根节点和新根节点，即根节点和根节点的左子节点，所以只需要对这两个节点执行 $updateHeight$ 函数。函数代码参考如下：

##### 更新二叉树高度
```
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
```
树的高度也就是左右子树的高度最大值加一，若无子树，则设置树高为零。


* **右右情况(RR)**

该情况与上面的**左左情况**具有对称性，对平衡二叉树执行插入或删除节点操作后，根节点的平衡因子变为 $-2$，根节点的右子节点平衡因子为 $-1$ 或 $0$，为了恢复二叉树的平衡，需要进行左旋，来使得新的左右子树高度区域平衡。

![RR](https://upload-images.jianshu.io/upload_images/9738807-6e8e244576192a9b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


如上图 $RR$ 所示，该情况下需要对平衡二叉树执行左旋操作：
1. 设置根节点 $root$ 的右子节点为新的根节点 $root_{new}$；
2. 将 $root_{new}$ 节点的左子树作为 $root$ 节点的右子树，将  $root$ 节点作为 $root_{new}$ 的左子树，即降低“右子树”高度，提升“左子树”高度，使得新的左右子树高度趋于平衡；

左旋操作后，平衡二叉树如图 ***balanced_RR*** 所示。

![balanced_RR](https://upload-images.jianshu.io/upload_images/9738807-3f7d44a6c19fb826.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

##### 左旋代码
```
# rotate from right to left with the right-child node as the axis
def rotateR2L(node):
    rightChild = node.rchild
    rightChild.lchild, node.rchild = node, rightChild.lchild  # rotate
    updateHeight(node)
    updateHeight(rightChild)
    return rightChild
```

左旋操作同右旋一样，只更改了原根节点和新根节点的平衡因子，所以只需要对这两个节点执行 $updateHeight$ 函数。

* **左右情况**

该情况下根节点的平衡因子与**左左情况**相同，都为 $2$，不同之处在于左子节点的平衡因子为 $-1$，若按照之前直接进行右旋操作，则旋转操作后二叉树扔处于不平衡状态。

对于图 ***LR***，节点 $B$ 的平衡因子为 $-1$，设 $B$ 节点的左子树 $D$ 高度为 $h$，则右子树 $E$ 高度为$h+1$，因为 $A$ 的平衡因子为 $2$，所以二叉树 $C$ 的高度为： $h$。则右旋操作后，$B$ 的左子树高度不变为 $h$，右子树高度为：$1+max(height(C),height(E))=h+2$，因为 $B$ 的平衡因子为 $-2$，所以按此方式的旋转操作没有效果。

![LR](https://upload-images.jianshu.io/upload_images/9738807-14452fac0451bffe.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

所以该情况下，首先需要对根节点的左子节点进行调整，即将左子节点的平衡因子由 $-1$ 调整为 $1$， 使得当前情况转换为 $LL$ 情况，然后再对二叉树执行右旋操作。

***step 1:对左子树执行左旋操作***

![step_1](https://upload-images.jianshu.io/upload_images/9738807-5c670d7c179f58e4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

***step 2:对二叉树执行右旋操作***

![step_2](https://upload-images.jianshu.io/upload_images/9738807-bf00a7e9bfbca0eb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


* **右左情况**

该情况与上面**左右情况**对称，根节点的平衡因子为 $-2$，右子节点平衡因子为 $1$，需要首先对右子树进行右旋操作，调整二叉树为 $RR$ 情况，再对二叉树执行左旋操作。

![RL](https://upload-images.jianshu.io/upload_images/9738807-a93c926911f15860.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

***step 1:对右子树执行右旋操作***


![step_1](https://upload-images.jianshu.io/upload_images/9738807-ab4b391b5ddd601c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


***step 2:对二叉树执行左旋操作***

![step_2](https://upload-images.jianshu.io/upload_images/9738807-63b0e87c9e1b0a8c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 性能分析

> 因为平衡二叉树也是二叉搜索树，回顾[二叉搜索树](https://www.jianshu.com/p/ff4b93b088eb)中的操作复杂度，查询、插入和删除复杂度均为 $log_2N$~$N$。平衡二叉树中查询复杂度影响因素自然为树的高度；插入节点操作可以拆分为两个步骤：查询节点位置，插入节点后平衡操作；删除节点操作同理可以拆分为两个步骤：查询节点位置，删除节点后平衡操作。
\
平衡调节过程中可能存在旋转操作，递归执行的次数则依赖于树的高度（可以优化为当前节点平衡因子不发生变化，则取消向上递归）。所以平衡二叉树中查询、插入和删除节点操作的复杂度依赖于树高。

平衡二叉树因为左右子树的平衡因子限制，所以不可能存在类似于斜树的情况，因为任一节点的左右子树高度差最大为一，且二叉树具有对称性，所以不妨设每个子树的左子树高度大于右子树高度。


![AVL](https://upload-images.jianshu.io/upload_images/9738807-277ea93a9497efc5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

根据平衡二叉树定义可知，若二叉树左子树高度为 $h$ $(h \ge 2)$，则右子树高度最少也要是 $h-1$，方能满足平衡二叉树的平衡特性。以 $F(H)$ 表示高度为 $H$ 的平衡二叉树的最少节点个数，若二叉树不是空树则有：

$F(0) = 1$
$F(1) = 2$
$F(2) = 4$
$F(H) = F(H-1)+F(H-2)+1 $ $(H \ge 3)$  

根据推导公式可知，平衡二叉树的高度最大为 $O(log_{\frac{1+\sqrt5}2}N)$。当二叉树向完全二叉树靠拢，尽量填满每层上的节点时，树的高度最小，为 $O(log_2N)$。所以相对于二叉搜索树，平衡二叉树避免了向线性结构演化的倾向，查询、插入和删除节点的时间复杂度为 $O(log_2N)$~$O(log_{\frac{1+\sqrt5}2}N)$。因为每个节点上需要保存平衡因子，所以空间复杂度要略高于二叉搜索树。

### 代码附录
> python版本：3.7，树中的遍历、节点插入和删除操作使用的是递归形式

* 树节点定义
```
# tree node definition
class Node(object):
    def __init__(self, value, height=0, lchild=None, rchild=None):
        self.lchild = lchild
        self.rchild = rchild
        self.value = value
        self.height = height   
```
相对于二叉搜索树的节点定义，增加了 $height$ 属性。

* 树定义
```
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
```
树结构定义与二叉搜索树中结构相同保持不变。

* 模块中对树结构中的函数进行实现
```
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
```
* 测试代码与输出
```
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
```
* 输出结果为：
```
BST in-order traversal------------------
0 height= 1, 1 height= 0, 2 height= 3, 3 height= 0, 4 height= 1, 5 height= 0, 6 height= 2, 7 height= 0, 8 height= 1, 9 height= 0, 
delete test------------------
after delete 7,BST in-order is = 0 height= 1, 1 height= 0, 2 height= 3, 3 height= 0, 4 height= 1, 5 height= 0, 6 height= 2, 8 height= 1, 9 height= 0, 
after delete 7,BST in-order is = 0 height= 1, 1 height= 0, 2 height= 3, 3 height= 0, 4 height= 1, 5 height= 0, 6 height= 2, 8 height= 1, 9 height= 0, 
after delete 9,BST in-order is = 0 height= 1, 1 height= 0, 2 height= 3, 3 height= 0, 4 height= 1, 5 height= 0, 6 height= 2, 8 height= 0, 
after delete 6,BST in-order is = 0 height= 1, 1 height= 0, 2 height= 3, 3 height= 0, 4 height= 1, 5 height= 2, 8 height= 0, 
after delete 8,BST in-order is = 0 height= 1, 1 height= 0, 2 height= 2, 3 height= 0, 4 height= 1, 5 height= 0, 
after delete 1,BST in-order is = 0 height= 0, 2 height= 2, 3 height= 0, 4 height= 1, 5 height= 0, 
after delete 2,BST in-order is = 0 height= 0, 3 height= 2, 4 height= 1, 5 height= 0, 
after delete 0,BST in-order is = 3 height= 0, 4 height= 1, 5 height= 0, 
after delete 4,BST in-order is = 3 height= 1, 5 height= 0, 
after delete 3,BST in-order is = 5 height= 0, 
after delete 5,BST in-order is = 
```
