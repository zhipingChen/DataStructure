
![](http://upload-images.jianshu.io/upload_images/9738807-5de5fd6ee70c4f7e.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1080/q/50)

邻接表和邻接矩阵是图的两种常用存储表示方式，用于记录图中任意两个顶点之间的连通关系，包括权值。

> 对于图 $G=(V, E)$ 而言，其中 $V$ 表示顶点集合，$E$ 表示边集合。

对于无向图 ***graph***，图的顶点集合和边集合如下：

$V = \{1,2,3,4,5\} $
$E =\{(1,2),(1,3),(1,4),(2,3),(3,4),(3,5)\} $

![graph](https://upload-images.jianshu.io/upload_images/9738807-115de93d1f79686a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

对于有向图 ***digraph***，图的顶点集合和边集合如下：

$V = \{1,2,3,4,5\} $
$E =\{<1,2>,<1,3>,<1,4>,<2,3>,<3,1>,<3,5>,<4,3>\} $

![digraph](https://upload-images.jianshu.io/upload_images/9738807-824248f02a5ec8f4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


### 邻接表

**无向图 graph 表示**

![graph_adjacency_list](https://upload-images.jianshu.io/upload_images/9738807-507325cbc3206d58.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


**有向图 digraph 表示**

![digraph_adjacency_list](https://upload-images.jianshu.io/upload_images/9738807-bac2031d9fcd4b52.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


若采用邻接表表示，则需要申请 $|V|$ 个列表，每个列表存储一个顶点出发的所有相邻顶点。如果图 $G$ 为有向图，则 $|V|$ 个列表存储的总顶点个数为 $|E|$；如果图 $G$ 为无向图，则 $|V|$ 个列表存储的总顶点个数为 $2 |E|$（暂不考虑自回路）。因为需要申请大小为 $|V|$ 的数组来保存节点，对节点分配序号，所以需要申请大小为 $|V|$ 的额外存储空间，即邻接表方式的存储空间复杂度为 $O(|V|+|E|)$。

### 邻接矩阵

**无向图 graph 表示**

![graph_adjacency_matrix](https://upload-images.jianshu.io/upload_images/9738807-153725979125f9da.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

**有向图 digraph 表示**

![digraph_adjacency_matrix](https://upload-images.jianshu.io/upload_images/9738807-08869f604e48d9ff.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

若采用邻接矩阵表示，则需要申请空间大小为 $|V|^2$ 的二维数组，在二位数组中保存每两个顶点之间的连通关系，则无论有向图或无向图，邻接矩阵方式的存储空间复杂度皆为 $O(|V|^2)$。若只记录图中顶点是否连通，不记录权值大小，则可以使用一个二进制位来表示二维数组的每个元素，并且根据无向图的特点可知，无向图的邻接矩阵沿对角线对称，所以可以选择记录一半邻接矩阵的形式来节省空间开销。

### 两种存储结构对比

根据邻接表和邻接矩阵的结构特性可知，当图为稀疏图、顶点较多，即图结构比较大时，更适宜选择邻接表作为存储结构。当图为稠密图、顶点较少时，或者不需要记录图中边的权值时，使用邻接矩阵作为存储结构较为合适。

### 代码附录

#####邻接表结构

```
# graph node definition
class Node(object):
    def __init__(self, index, weight, next = None):
        self.index = index
        self.weight = weight
        self.next = next

# adjacency list definition
class AdjacencyList(object):
    def __init__(self, number):
        self.number = number
        self.list = [None] * number

    # insert node
    def insert(self, origin, index, weight = 1):
        node = Node(index, weight, self.list[origin - 1])
        self.list[origin - 1] = node
```
测试代码：
```
if __name__ == '__main__':
    graph = AdjacencyList(5)
    graph.insert(1, 2)
    graph.insert(1, 3)
    graph.insert(1, 4)
    graph.insert(2, 3)
    graph.insert(3, 1)
    graph.insert(3, 5)
    graph.insert(4, 3)
    for i in range(graph.number):
        print('node', (i + 1), 'links:', end = ' ')
        node = graph.list[i]
        while node:
            print(node.index, end = ' ')
            node = node.next
        print()
```
输出结果：
```
node 1 links: 4 3 2 
node 2 links: 3 
node 3 links: 5 1 
node 4 links: 3 
node 5 links: 
```

#####邻接矩阵结构

```
# adjacency list definition
class AdjacencyMatrix(object):
    def __init__(self, number):
        self.number = number
        self.list = [[None] * number for i in range(number)]

    # insert node
    def insert(self, origin, index, weight = 1):
        self.list[origin - 1][index - 1] = weight
```
测试代码：
```
if __name__ == '__main__':
    graph = AdjacencyMatrix(5)
    graph.insert(1, 2)
    graph.insert(1, 3)
    graph.insert(1, 4)
    graph.insert(2, 3)
    graph.insert(3, 1)
    graph.insert(3, 5)
    graph.insert(4, 3)
    for i in range(graph.number):
        print('node', (i + 1), 'links:', end = ' ')
        j = 0
        while j < graph.number:
            print(j + 1, end = ' ') if graph.list[i][j] else None
            j += 1
        print()
```
输出结果：
```
node 1 links: 2 3 4 
node 2 links: 3 
node 3 links: 1 5 
node 4 links: 3 
node 5 links: 
```
