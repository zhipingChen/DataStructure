![](https://upload-images.jianshu.io/upload_images/9738807-2e322d8379cb8ac4.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 遍历方式
二叉树的常见遍历方式如下几种：
* **前序遍历：** 访问根节点，前序遍历方式访问左子树，前序遍历方式访问右子树；
* **中序遍历：** 中序遍历方式访问左子树，访问根节点，中序遍历方式访问右子树；
* **后序遍历：** 后序遍历方式访问左子树，后序遍历方式访问右子树，访问根节点；
* **层次遍历：** 按照层次递增的顺序，依次访问树的每层节点。

### 示例演示

> 除去层次遍历不谈，根据其他三种遍历方式的描述可发现，其描述的内容也就是递归进行遍历的过程。

##### 二叉树示例：

![Binary Tree](https://upload-images.jianshu.io/upload_images/9738807-a27b41ec37341a23.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

##### 前序遍历

前序遍历的方式，也就是对每一棵子树，按照根节点、左子树、右子树的顺序进行访问，也就是根-左-右的访问顺序。因为每一棵非空子树，又可拆分为根节点、左子树和右子树，所以可以按照根-左-右的方式，递归访问每棵子树。

**递归方式：**
```
#recursive pre-order traversal
def recursive_pre_order_traversal(root):
    if not root:
        return
    print(root.value,end=' ')
    recursive_pre_order_traversal(root.lchild)
    recursive_pre_order_traversal(root.rchild)
```

![pre-order](https://upload-images.jianshu.io/upload_images/9738807-96fd9183b5f717b1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

观察二叉树的前序递归遍历方式，首先访问 “5” 节点，然后是 “3” 节点，然后是 “0” 节点，然后是 “0” 节点右子树 A （A 子树递归访问），然后是 “3” 节点的右子树 B （即进行回溯，B 子树同 A 子树，递归访问）。

通过以上过程可以发现：

* A、B 子树的节点访问方式，与以 “5” 为根节点的二叉树访问方式相同，即：5 $\to$ 3 $\to$ 0 $\to$ A $\to$ B。
* 由 A 子树到 B 子树的访问过程即为回溯，示例代码中回溯的实现，使用了递归的形式，递归的函数会形成调用栈，每个函数的调用会保存一个栈帧，通过栈帧中数据的保存，来完成回溯。


所以这里前序递归遍历规则 “根-左-右” 的体现包括两个环节：
* 递归：前序访问的递归顺序即为根-左-右。
步骤：
1.访问二叉树 $T$ 的根节点 $root$；
2.若 $root$ 左子树非空，则二叉树 $T$ 指向 $root$ 左子树，执行步骤 1；
3.若 $root$ 左子树为空，则二叉树 $T$ 指向 $root$ 右子树，执行步骤 1；

* 回溯：一个子树的递归结束后，返回上一层（非父节点那一层）继续递归，即为回溯。
例如以 0 为根节点，右子树为 A 的二叉树，完成前序遍历后，也就相当于以 3 为根节点，{0, A} 为左子树，B 为右子树的二叉树，刚刚完成根-左-右前序遍历中的，“左”这一步，下一个访问的二叉树即为 B。

根据以上过程，可以推出前序遍历的非递归形式。

**非递归方式：**
```
#non_recursive pre-order traversal
def non_recursive_pre_order_traversal(root):
    stack = []
    while root or len(stack) > 0:
        if root:  
            print(root.value,end=' ')
            stack.append(root)
            root = root.lchild
        else:  
            root = stack.pop()
            root = root.rchild
```
以上非递归代码中，通过循环的形式完成了类似于递归的调用，通过栈对象完成回溯。代码循环执行过程为：若二叉树根节点存在，则访问根节点，然后以相同方式访问根节点的左子树；若根节点不存在，则返回上一层访问右子树。

![tips](https://upload-images.jianshu.io/upload_images/9738807-0c4ee6b8b7db02be.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


***tips：***

1.前序和中序的回溯操作，都是访问上一层的右子树，因为无论是根-左-右，或者左-根-右，右子树访问结束后，都表示根节点和左子树已经访问过。

2.上一层不一定是父节点那一层，若二叉树 $C_1$ 是根节点 $B$ 的左子树，则左子树访问结束，上一层即为父节点一层，也就是根节点 $B$ 这一层，下一步访问根节点 $B$ 的右子树 $C_2$；若二叉树 $C_2$ 访问结束，则表示根节点 $B$ 和左子树 $C_1$ 已经访问结束，上一层为根节点 $A$ 这一层，下一步访问即为二叉树 $D$ 。

代码中使用栈来保存上一层的节点，即栈中最后一个元素即为上一层的根节点，通过出栈操作来完成回溯。

##### 中序遍历

中序遍历二叉树顺序为左子树-根节点-右子树形式。如果二叉树为二叉搜索树这样的节点有序结构，则中序遍历输出为有序的节点列表。

**递归方式：**
```
#recursive in-order traversal
def recursive_in_order_traversal(root):
    if not root:
        return
    recursive_in_order_traversal(root.lchild)
    print(root.value,end=' ')
    recursive_in_order_traversal(root.rchild)
```

在非递归形式中，所谓的访问其实就是入栈和输出根节点值的操作，因为要借用栈对象来实现回溯，所以访问每棵二叉树时，入栈根节点的操作是不变的。区别只在于中序遍历时，输出根节点的操作放在了访问右子树前，而非前序遍历的入栈操作时输出。

**非递归方式：**
```
#non_recursive in-order traversal
def non_recursive_in_order_traversal(root):
    stack = []
    while root or len(stack) > 0:
        if root:
            stack.append(root)
            root = root.lchild
        else:
            root = stack.pop()
            print(root.value,end=' ')
            root = root.rchild
```
观察前序遍历和中序遍历的非递归方式可以发现，两者除了输出操作 ***print*** 语句位置不同外，其他内容完全一样。

##### 后序遍历

后序遍历二叉树顺序为左子树-右子树-根节点形式。

**递归方式：**
```
#recursive post-order traversal
def recursive_post_order_traversal(root):
    if not root:
        return
    recursive_post_order_traversal(root.lchild)
    recursive_post_order_traversal(root.rchild)
    print(root.value,end=' ')
```
因为要完成回溯，所以根节点入栈的操作不变。后序遍历的顺序为：左-右-根，也就是右子树访问结束后才会执行根节点的输出操作，即右子树遍历结束后返回上一层继续遍历，后序遍历中的上一层就是父节点一层。与前序和中序遍历不同之处在于，后序遍历在根节点的输出上需要多做一些工作。

![BT](https://upload-images.jianshu.io/upload_images/9738807-fe12846c0a861bc0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

分析上图 BT 中的两颗二叉树：
【1】树 bt1 中，二叉树 $C$ 遍历结束后，输出上一层的根节点 $B$ 的值。因为 $B$ 节点是其上一层的左节点，也就是说以 $A$ 为根节点的二叉树，完成了后序遍历的左子树遍历，所以再下一步访问右子树 $D$。
【2】树 bt2 中，二叉树 $H$ 遍历结束后，输出上一层的根节点 $G$ 的值。因为 $G$ 是其上一层的右节点，所以 $G$ 为根节点的二叉树遍历结束后，下一步输出 $G$ 的上一层的根节点 $E$ 的值。因为 $E$ 是其上一层的左节点，也就是说以 $T$ 为根节点的二叉树，完成了后序遍历的左子树遍历，所以再下一步访问右子树 $K$。

根据以上两个二叉树的后序遍历过程可以发现，右子树遍历结束后输出根节点的值，虽然完成了一轮的左-右-根遍历，但并不算操作结束。还要判断根节点 $root_i$ 是其上一层根节点 $root_{i-1}$ 的左节点还是右节点：
* 若 $root_i$ 是 $root_{i-1}$ 的左节点，则说明 $root_{i-1}$ 一层完成了左-右-根的左子树遍历，下一步访问 $root_{i-1}$ 的右子树；
* 若 $root_i$ 是 $root_{i-1}$ 的右节点，则说明 $root_{i-1}$ 一层完成了左-右-根的右子树遍历，下一步访问输出 $root_{i-1}$ 的值，并判断 $root_{i-1}$ 是其上一层根节点 $root_{i-2}$ 的左节点还是右节点。

根据遍历完成的二叉树的根节点是其上一层根节点的左节点或右节点的不同，进行迭代处理。其实就是迭代输出根节点的值，直到根节点是其上一层根节点的左节点，则输出根节点并访问上一层根节点的右子树。

 **非递归方式：**
```
#non_recursive post-order traversal
def non_recursive_post_order_traversal_one(root):
    stack = []
    while root or len(stack) > 0:
        if root:
            stack.append(root)
            root = root.lchild
        else:
            if stack[-1].rchild:
                root = stack[-1].rchild
            else:
                while len(stack) > 1 and stack[-1] == stack[-2].rchild:
                    print(stack.pop().value, end=' ')
                print(stack.pop().value, end=' ')
                if len(stack) > 0:
                    root = stack[-1].rchild
```
观察代码可知，循环处理的入栈部分跟前序和中序一样，不同之处在于二叉树遍历结束后，会对根节点进行迭代输出。

后续遍历有一种简洁的写法形式，后序遍历顺序为：左-右-根，可以另声明一个列表倒序保存根-右-左顺序的记录，下面给个简写的示例：

 **非递归方式_简洁形式：**
```
# non_recursive post-order traversal
def non_recursive_post_order_traversal_two(root):
    stack = []
    save_list = []
    while root or len(stack) > 0:
        if root:
            stack.append(root)
            save_list.insert(0,root.value)
            root = root.rchild
        else:
            root = stack.pop()
            root = root.lchild
    print(save_list,end=' ')
```
代码比较简单，跟前序遍历形式基本一致。

##### 层次遍历

层次遍历就是按层递增的顺序输出每层的节点，即顺序的输出每层节点的左、右子节点。这里借助具有先进先出特性的队列对象完成遍历。

 **代码示例：**
```
#hierarchical traversal
def hierarchical_traversal(root):
    node_queue = queue.Queue()
    node_queue.put(root)
    while node_queue.qsize() > 0:
        root = node_queue.get()
        print(root.value,end=' ')
        if root.lchild:
            node_queue.put(root.lchild)
        if root.rchild:
            node_queue.put(root.rchild)
```
层次遍历的逻辑比较简单，即顺序记录每层节点，主要利用了队列先进先出的特性。

##### 附录

以上是四种遍历方式的描述和代码示例，下面给出测试和输出。其中树结构 $Tree$ 引用自 [二叉搜索树](https://www.jianshu.com/p/ff4b93b088eb) 中定义。
```
if __name__ == '__main__':
    arr = [5, 3, 4, 0, 2, 1, 8, 6, 9, 7]
    T = Tree()
    for i in arr:
        T.insert(i)

    print('BST recursive pre-order traversal:',end=' ')
    recursive_pre_order_traversal(T.root)
    print('\nBST non_recursive pre-order traversal:',end=' ')
    non_recursive_pre_order_traversal(T.root)

    print('\n\nBST recursive in-order traversal:',end=' ')
    recursive_in_order_traversal(T.root)
    print('\nBST non_recursive in-order traversal:',end=' ')
    non_recursive_in_order_traversal(T.root)

    print('\n\nBST recursive post-order traversal:',end=' ')
    recursive_post_order_traversal(T.root)
    print('\nBST non_recursive post-order traversal method one:',end=' ')
    non_recursive_post_order_traversal_one(T.root)
    print('\nBST non_recursive post-order traversal method two:',end=' ')
    non_recursive_post_order_traversal_two(T.root)

    print('\n\nBST hierarchical traversal:',end=' ')
    hierarchical_traversal(T.root)
```
输出结果为：
```
BST recursive pre-order traversal: 5 3 0 2 1 4 8 6 7 9 
BST non_recursive pre-order traversal: 5 3 0 2 1 4 8 6 7 9 

BST recursive in-order traversal: 0 1 2 3 4 5 6 7 8 9 
BST non_recursive in-order traversal: 0 1 2 3 4 5 6 7 8 9 

BST recursive post-order traversal: 1 2 0 4 3 7 6 9 8 5 
BST non_recursive post-order traversal method one: 1 2 0 4 3 7 6 9 8 5 
BST non_recursive post-order traversal method two: [1, 2, 0, 4, 3, 7, 6, 9, 8, 5] 

BST hierarchical traversal: 5 3 8 0 4 6 9 2 7 1
```
