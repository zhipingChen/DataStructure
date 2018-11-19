![](http://upload-images.jianshu.io/upload_images/9738807-4436048af6ed0de0.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1080/q/50)




> [```Bellman-Ford```](https://www.jianshu.com/p/b876fe9b2338) 算法或者 [```Dijkstra```](https://www.jianshu.com/p/152427566911) 算法用于解决单源最短路径问题，获取从指定起点出发，到达图中各个顶点的最短路径。若要获得图中每两个顶点之间的最短路径，则需要对算法执行 $|V|$ 次，不过这里推荐另一种获得每对顶点间最短路径的方式。

```Floyd-Warshall``` 算法使用动态规划策略计算图中每两个顶点间的最短路径，算法中通过调整路径中经过的中间顶点来缩小路径权值，最终得到每对顶点间的最短路径。

> ```Floyd``` 算法允许图中存在负权边，但是不能存在负权回路。

### 算法介绍

对于图 $G=(V,E)$，以 $V=\{1,2,...,n\}$ 表示顶点集合，则从顶点 $i$ 到顶点 $j$ 的最短路径中经过的所有顶点都处于集合 $V$ 中。对于顶点集合 $K=\{1,2,..,k\}$，不妨以 $D_{i,j}^k$ 表示从顶点 $i$ 到顶点 $j$ 的最短路径权值，且路径中经过的顶点都处于集合 $K$ 中。因此当 $k\neq n$ 时，因为此时的最短路径并非基于全部顶点集合，所以此时的 $D_{i,j}^k$ 值可能要大于 $D_{i,j}^n$。当 $k = n$ 时，则有 $D_{i,j}^k=D_{i,j}^n=\delta(i,j)$，即此时的最短路径才是基于顶点集合 $V$ 上真正的最短路径权值。

> 根据最短路径的特性，若从顶点 $a$ 到顶点 $c$ 的最短路径为 $p=\langle a,v_1,v_2,b,v_3,v_4,c\rangle$，则路径 $\langle a,v_1,v_2,b\rangle$ 为顶点 $a$ 到顶点 $b$ 的最短路径，因为若 $a,b$ 之间存在权值更小的路径，则顶点 $a,c$ 的最短路径 $p$ 不成立，同理，路径 $\langle b,v_3,v_4,c\rangle$ 为顶点 $b$ 到顶点 $c$ 的最短路径。

对于顶点集合 $K=\{1,2,..,k\}$，若顶点 $i$ 到顶点 $j$ 的最短路径中不包含顶点 $k$，则有 $D_{i,j}^k=D_{i,j}^{k-1}$；若最短路径中包含顶点 $k$，则有 $D_{i,j}^k=D_{i,k}^{k-1}+D_{k,j}^{k-1}$。若 $k=0$，则 $D_{i,j}^k=w(i,j)$，表示顶点 $i$ 和顶点 $j$ 之间的路径上不存在其他顶点，路径权值即为边权值。

因此有如下递推关系式：

$$
D_{i,j}^k=
\begin{cases}
w(i,j) & k=0 \\
min(D_{i,j}^{k-1},D_{i,k}^{k-1}+D_{k,j}^{k-1}) & k \ge 1 
\end{cases}
$$

### 算法过程

根据该递推关系可知，对于任意两个顶点 $i,j$，可以递增 $k$ 值来逐渐获得最终的最短路径权值 $D_{i,j}^n$。所以在算法的实现中，可以设置一个 $n \times n$ 二维矩阵，用于保存每两个顶点之间的路径权值，递增 $k$ 值，遍历更新矩阵每个元素的路劲权值，当 $k=n$ 时，此时矩阵中存储的则是任意顶点 $i,j$ 之间的最短路径权值。

### 演示示例

![graph](https://upload-images.jianshu.io/upload_images/9738807-3d6a7f92e773a41b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


![matrix](https://upload-images.jianshu.io/upload_images/9738807-9d554759cf894d00.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

根据图 ```graph``` 构造矩阵 ```matrix```，其中顶点到自身的距离为 0，每两个顶点之间边的权值如 ```matrix``` 所示。

当 $k=1$ 时，根据推导关系式 $D_{i,j}^k=min(D_{i,j}^{k-1},D_{i,k}^{k-1}+D_{k,j}^{k-1})$ 遍历更新矩阵元素，更新后，矩阵如下图所示：

![matrix_1](https://upload-images.jianshu.io/upload_images/9738807-9d554759cf894d00.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

随便元素值并没有发生变化，但此时对于任意顶点 $i,j$，矩阵 ```matrix_1``` 中存储的都是 $D_{i,j}^1$ 的值，表示任意两个顶点在中间顶点处于集合 $\{1\}$ 上的最短路径权值。

递增 $k$ 值，当 $k=9$ 时，矩阵元素如下图所示：

![matrix_8](https://upload-images.jianshu.io/upload_images/9738807-e20f30424ae08b40.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

此时矩阵 ```matrix_9``` 中存储的都是 $D_{i,j}^9$ 的值，表示任意两个顶点在中间顶点处于集合 $V=\{1,2,3,4,5,6,7,8,9\}$ 上的最短路径权值，即此时对于任意两个顶点有 $D_{i,j}^9=\delta(i,j)$。

### 算法示例

```
def floyd(graph):
    matrix = graph.list
    for k in range(graph.number):
        for i in range(graph.number-1,-1,-1):
            for j in range(graph.number):
                if matrix[i][k] != None and matrix[k][j] != None and (matrix[i][j] == None or matrix[i][k] + matrix[k][j] < matrix[i][j]):
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
```
```floyd``` 算法较为简洁，代码中存在三层循环，第二层和第三层循环为遍历矩阵每个元素，根据递推关系式，更新每两个顶点之间的路径权值。第一层循环则是递增 $k$ 值，直到 $k=graph.number$，此时更新矩阵元素，可以获得基于整个顶点集合上的最短路径权值。


### 性能分析

```floyd``` 算法中存在三层循环，所以时间复杂度为 $O(|V|^3)$。

### 代码附录

[Floyd算法代码及测试结果](./floyd.py)