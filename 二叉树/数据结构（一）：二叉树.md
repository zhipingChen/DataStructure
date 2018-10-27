

![](https://upload-images.jianshu.io/upload_images/9738807-617a69ff54160e51.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



## 定义 ##

二叉树( binary tree )是有限节点集合构成的结构，其结构的递归定义为：

* **三个不相交的节点集合构成，一个作为根节点，一个节点集构成的二叉树作为根节点的左子树，另一个节点集构成的二叉树作为根节点的右子树**
* **当节点数为零时，表示二叉树为空**

所以节点个数为零的空树也是二叉树，二叉树根节点的左、右子树也是二叉树，其结构同样符合以上定义，当左子树为空树时，表示根节点没有左子节点。且二叉树区分左、右子树，以下两个二叉树为不同的二叉树。

![one](https://upload-images.jianshu.io/upload_images/9738807-204dba5ac0724172.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


![another one](https://upload-images.jianshu.io/upload_images/9738807-6f95ddb7366d098f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)




## 结构特性 ##

首先说明下几个概念：
* 根节点： 没有父节点的节点；
* 叶子节点： 没有子节点的节点；
* 节点的度 ：节点的分支个数，二叉树每个节点的分支个数为 0~2；
* 路径：连接节点和后代子节点之间的不重复边；
* 节点的深度：从根节点到该节点的路径长；
* 节点的高度：从该节点到叶子节点的最大路径长；
* 节点的层数：父节点的层数加一；
* 树的高度：根节点高度。
* 树的深度：叶子节点深度的最大值。
---
**关于高度和深度的起始值 0 或 1 的个人看法：**

> 对于深度、高度和层数的起点值，可能有些地方基数是从1开始计算的。对于这个起点值的设置，个人觉得如果你高兴，从10086开始也无妨，因为在应用中，这些数据量只是为了方便计算，起作用的只是相对值而已。

> 为了方便理解，这里设置基数为0，深度可以认为是从水平面，也就是0深度，往下有几层，深度就是几；高度类似理解，地平面是0，往上有几层，高度就是几。

参考下图：

![](https://upload-images.jianshu.io/upload_images/9738807-d56675b86c397232.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

图片来源：[What is the difference between tree depth and height?](https://stackoverflow.com/questions/2603692/what-is-the-difference-between-tree-depth-and-height)

---
## 满二叉树、完全二叉树、完美(理想)二叉树 ##

> 关于完全二叉树和满二叉树的定义，因为最初翻译的不同，已经混淆很久了，所以已经属于一个历史问题了。这里尽量不去分辨哪一种定义是正确的，只按照个人的理解去描述。
* **满二叉树( Full Binary Tree )：**
  每个节点的度为 0 或 2，即除了叶子节点，每个节点都有两个子节点。

示例：

![Full Binary Tree](https://upload-images.jianshu.io/upload_images/9738807-9813b543f853e05e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)




* **完全二叉树( Complete Binary Tree )：**
  除深度最大的一层外，其他每层上的节点都是填充满的，且深度最大的一层节点分布从左向右是连续无间隔的。

示例：

![Complete Binary Tree](https://upload-images.jianshu.io/upload_images/9738807-873a6c1adab9356c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

* **完美/理想二叉树( Perfect Binary Tree )：**
  除叶子节点外，每个节点度都为 2，且叶子节点在同一层。

示例：

![Perfect Binary Tree](https://upload-images.jianshu.io/upload_images/9738807-254970d20eb9c289.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

以上概念参考：
* [Binary tree](https://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees)
* [Binary Tree | Set 3 (Types of Binary Tree)](https://www.geeksforgeeks.org/binary-tree-set-3-types-of-binary-tree/)
---
## 二叉树数据量 ##
下面介绍二叉树几个数据量之间的关系，变量声明如下：
> $d$：树的高度
 $n$：节点总数
 $n_0$：度为 0 的节点个数，即叶子节点个数
 $n_1$：度为 1 的节点个数
 $n_2$：度为 2 的节点个数
 $l_i$：第 $i$ 层上节点个数

* **完美二叉树中，第 $d$ 层上节点个数为：$l_d=2^{d}$**
*proof：*
1.第 0 层上，只有根节点，所以 0 层节点个数为：$l_0= 2^0$ ;
2.每层节点度都为 2 ，所以下一层的节点个数为：$l_i=l_{i-1}*2$；
3.所以第 $d$ 层节点个数为：$l_d= l_{d-1}*2=l_0*2^{d}$。

* **深度为 $d$ 的完美二叉树，节点总数为：$n=2^{d+1}-1$** 
*proof：*
1.每层的节点个数 $\{l_i\}$ 构成等比数列，公比为： $q=2$；
2.第 0 层节点个数 $l_0=1$，所以总节点个数为：$n=l_0 \frac {1-q^{d+1}}{1-q}=2^{d+1}-1$ 

* **深度为 $d$ 的完美二叉树，非叶子节点和叶子节点的个数有：$n-n_0=n_0-1$，节点总数与叶子节点个数有：$n=2*n_0-1$** 
*proof：*
深度为 $d$ 的完美二叉树，则 $d$ 层节点即为叶子节点，即：$l_d=n_0$，由以上结论可知，深度为 $d$ 的完美二叉树，叶子节点个数为 $l_d=2^{d}$，总节点个数为 $n=2^{d+1}-1$，所以非叶子节点个数为：$n-n_0=n-l_d=2^{d+1}-1-2^{d}=2^{d}-1=n_0-1$，即：$n-n_0=n_0-1$，$n=2*n_0-1$

* **对于普通的非空二叉树，叶子节点个数 $n_0$ 与度为 2 的节点个数 $n_2$ 关系为：$n_0=n_2+1$** 
*proof：*
1.设度为 1 的节点个数为 $n_1$，则节点总数 $n=n_0+n_1+n_2$
2.设二叉树中边的个数为 $e$，有如下关系：
 【1】树中除根节点外，每个节点都存在该节点到其父节点的一条边，即除根节点外，每个节点都对应着一条边，则有关系：$e=n-1$
【2】树中每个节点度，表示该节点的子节点个数，也表示着该节点对应的边的个数，则有关系：$e=n_1+2*n_2$
根据【1】【2】可知，有关系：$n-1=n_1+2*n_2$，根据 1 中 $n=n_0+n_1+n_2$，则有： $n_0+n_1+n_2-1=n_1+2*n_2$，即：$n_0=n_2+1$，二叉树中叶子节点个数为度为 2 的节点个数加 1。
