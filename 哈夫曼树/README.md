![](https://upload-images.jianshu.io/upload_images/9738807-c6c746977f7fa8c1.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


### 哈夫曼树

哈夫曼树（或者赫夫曼树、霍夫曼树），指的是一种满二叉树，该类型二叉树具有一项特性，即树的带权路径长最小，所以也称之为最优二叉树。

> 节点的带权路径长指的是叶子节点的权值与路径长的乘积，树的带权路径长即为树中所有叶子节点的带权路径长度之和。由此可知，若叶子节点的权值都是已知的，则二叉树的构造过程中，使得权值越大的叶子节点路径越小，则整棵树的带权路径长最小。

### 编码与解码

数据在计算机上是以二进制表达的，即计算机只识别二进制序列，所以所有字符内容都需要完成与二进制的转换，才能在计算机中存储和呈现为我们看到的内容。并且这种转换方式必须是一致的，即字符内容若以方式 $A$ 转换为二进制序列，则二进制序列同样需要以方式 $A$ 转换为字符内容，否则会产生所谓的乱码现象。这种字符到二进制的转换即为编码，二进制到字符的转换即为解码，编码和解码需要使用相同的映射规则，才不会产生乱码。

### 哈夫曼编码

构造哈夫曼树的目的是为了完成哈夫曼编码，哈夫曼编码是一种变长、极少多余编码方案。相对于等长编码，将文件中每个字符转换为固定个数的二进制位，变长编码根据字符使用频率的高低，使用了不同长度的二进制位与不同字符进行映射，使得频率高的字符对应的二进制位较短，频率低的字符对应的二进制位较长。使得源文件利用哈夫曼编码后的二进制序列大小，相对于原编码方案能够有较大缩小，如此即完成了文件的压缩。

哈夫曼编码能够用于实现文件的无损压缩，自然保证了文件解压缩过程的正确性，即二进制序列向字符的映射过程不会发生错乱。解码过程的正确性通过哈夫曼树的结构可以得到证明，以哈夫曼树中的每个叶子节点作为一个字符，则从根节点到每个叶子的路径都是唯一的，即不存在一个叶子节点的路径是另一个叶子节点的路径前缀。满足该特性的编码称之为前缀编码，所以哈夫曼编码中能够实现二进制到字符的正确映射。

### 哈夫曼树的构造

哈夫曼树是一棵满二叉树，树中只有两种类型的节点，即叶子节点和度为 2 的节点，所以树中任意节点的左子树和右子树同时存在。构建步骤如下：

1. 对字符集合按照字符频率进行升序排序，并构建一颗空树；
2. 遍历字符集合，将每一个字符添加到树中，添加规则为：
【1】若树为空，则作为根节点；
【2】若字符频率不大于根节点频率，则字符作为根节点的左兄弟，形成一个新的根节点，频率值为左、右子节点之和；
【3】若字符频率大于根节点频率，则字符作为根节点的右兄弟，形成一个新的根节点，频率值为左右子节点之和。


##### 构造示例

> 这里自然不可能以所有字符集作示例，假设字符集范围为 $A$~$J$
字符集合为：$contentArr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']$
对应的频率为：$valueArr = [5, 3, 4, 0, 2, 1, 8, 6, 9, 7]$

***step 1:***

对字符集合按照频率进行排序，这里使用[插入排序](https://www.jianshu.com/p/c156fe81ff06)算法进行排序。

**算法示例：**

```
# synchronise sort the valueArr and contentArr
def insertionSort(valueArr, contentArr):
    for i in range(1, len(valueArr)):  # iteration times
        tmpValue = valueArr[i]
        tmpContent = contentArr[i]
        while i > 0 and tmpValue < valueArr[i - 1]:
            valueArr[i] = valueArr[i - 1]
            contentArr[i] = contentArr[i - 1]
            i = i - 1
        valueArr[i] = tmpValue
        contentArr[i] = tmpContent
```

排序后字符集合和对应的频率为：
> $contentArr = ['D', 'F', 'E', 'B', 'C', 'A', 'H', 'J', 'G', 'I']$
$valueArr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]$

***step 2:***

遍历将集合中元素添加到树中，其中定义如下：

**树节点定义为：**
```
# tree node definition
class Node(object):
    def __init__(self, value, content=None, lchild=None, rchild=None):
        self.lchild = lchild
        self.rchild = rchild
        self.value = value
        self.content = content
```

**树定义为：**
```
# tree definition
class Tree(object):
    def __init__(self, root=None):
        self.root = root
        self.codeMap = {}

    # merge two nodes and return one root node
    def acceptNewNode(self, value, content):
        if not self.root:
            self.root = Node(value, content)
        else:
            newNode = Node(value, content)
            newRoot = Node(self.root.value + value)
            lchild, rchild = (self.root, newNode) if self.root.value < value else (newNode, self.root)
            newRoot.lchild, newRoot.rchild = lchild, rchild
            self.root = newRoot
```

树结构中定义的 $acceptNewNode$ 方法，用于向树中添加新字符，其中 $value$ 表示新字符的频率，$content$ 表示字符体。

> 第一个元素 $D$，频率为 $0$

![](https://upload-images.jianshu.io/upload_images/9738807-391b4b421c8619c7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> 第二个元素 $F$，频率为 $1$

![](https://upload-images.jianshu.io/upload_images/9738807-1bd963a69b8679b8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> 第三个元素 $E$，频率为 $2$

![](https://upload-images.jianshu.io/upload_images/9738807-848342fb7fea0533.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

...
...
...


> 第十个元素 $I$，频率为 $9$

![](https://upload-images.jianshu.io/upload_images/9738807-604c3fb65e241fa6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 哈夫曼树编解码

哈夫曼树构造完成之后，以 $0$ 表示左分支，$1$ 表示右分支，则树中每个字符都有唯一的二进制映射。这里借用哈希表结构，将字符与对应的二进制序列存储为键值对，来演示编码过程；利用二进制序列在二叉树中查找具体的字符，来演示解码过程。

##### 构造哈希表

首先根据哈夫曼树，生成哈希表，有点类似于前序遍历：

```
# initialize the huffman tree code map
def initializeCodeMap(node, byteArr, codeMap):
    if node.lchild:
        byteArr.append('0')
        initializeCodeMap(node.lchild, byteArr, codeMap)
        byteArr.append('1')
        initializeCodeMap(node.rchild, byteArr, codeMap)
        byteArr.pop() if len(byteArr) > 0 else None  # in case only the root node left
    else:
        codeMap[node.content] = ''.join(byteArr)
        byteArr.pop()
```

代码中以 $codeMap$ 作为存储键值对的哈希表， 以 $byteArr$ 存储二进制路径信息。因为哈夫曼树是满二叉树，节点的左子树存在则右子树同时存在，所以判断左子树是否存在即可判断是否为叶子节点。每个左叶子节点访问结束则记录键值对到 $codeMap$ 中，并将路径 $byteArr$ 回退到父节点，开始访问右子树；每个右叶子节点访问结束则记录键值对到 $codeMap$ 中，并将路径 $byteArr$ 回退到父节点的父节点，访问其右子树。

##### 编码与解码

构造完成哈希表后，编码 $encode$ 过程只需要根据字符取二进制序列即可。解码 $decode$ 过程就是根据二进制序列，不断在二叉树中查找字符而已，找到字符后则从根节点继续查找下一个字符。

编码与解码函数体实现如下：
```
# tree definition
class Tree(object):

    # encode
    def encode(self, chars):
        bytes = ''
        for i in chars:  # get the mapped bytes
            bytes += self.codeMap.get(i.upper(), '###')
        return bytes

    # decode
    def decode(self, bytes):
        chars = ''
        tmpNode = self.root
        for i in bytes:
            if i == '0':
                tmpNode = tmpNode.lchild
            elif i == '1':
                tmpNode = tmpNode.rchild
            if not tmpNode.lchild:
                chars += tmpNode.content
                tmpNode = self.root
        return chars
```

### 代码附录

[哈夫曼树代码及测试结果](./huffman.py)
