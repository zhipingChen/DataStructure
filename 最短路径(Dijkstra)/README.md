![](http://upload-images.jianshu.io/upload_images/9738807-265addbf94248e6c.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1080/q/50)




> 通过上一章[```最短路径(Bellman-Ford算法)```](https://www.jianshu.com/p/b876fe9b2338)的内容可知，```Bellman-Ford``` 算法是通过重复对边集执行松弛函数，来逐渐获得从起点到各个顶点的最短路径。并且对边的松弛顺序是随意进行的，所以才有最好情况和最坏情况之分。一般情况下则是通过不断的对边集进行重复松弛，来“堆”出从起点到其他顶点的最短路径，这种“盲目”的松弛存在极多的无效操作和时间浪费。

```Dijkstra``` 算法使用贪心策略计算从起点到指定顶点的最短路径，通过不断选择距离起点最近的顶点，来逐渐扩大最短路径权值，直到覆盖图中所有顶点。

> ```Dijkstra``` 算法前提为图中边的权值非负，若将最短路径中经过的顶点个数称为最短路径长度，则最短路径长度与最短路径权值呈正相关。而在 ```Bellman-Ford``` 算法中，因为边的权值可能为负，所以最短路径长度较大的顶点，其最短路径权值不一定更大。所以与 ```Bellman-Ford``` 算法相似，```Dijkstra``` 算法的计算最短路径过程，也是呈现一种波纹扩散的方式，不同之处在于，```Bellman-Ford``` 算法扩散过程中，逐渐增大的半径为最短路径长度，而 ```Dijkstra``` 算法的扩大半径为最短路径权值。

```Dijkstra``` 算法过程中也存在对边的松弛行为，不过该松弛过程并非“盲目”的对所有边进行松弛，而是对于已确认顶点为出度，未确认顶点为入度的边进行松弛。因为 ```Dijkstra``` 算法过程中每个顶点被确认一次，所以整个算法过程只需要对边集执行一次松弛，即边的松弛复杂度为 $O(|E|)$。

### 算法过程

1. 从未确认顶点中选择距离起点最近的顶点，并标记为已确认顶点
2. 根据步骤 1 中的已确认顶点，更新其相邻未确认顶点的距离
3. 重复步骤 1,2，直到不存在未确认顶点

### 演示示例

![graph](https://upload-images.jianshu.io/upload_images/9738807-2014d2279451f1f8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> 以图 ```graph``` 为例，边的权值如图中所示，初始化各顶点距离起点权值为 ```None```，不妨随机选择一个顶点作为起点，初始化起点的权值为 0

选择距离起点最近的顶点为已确认顶点，并更新该顶点的相邻未确认顶点距离

***step 1：***

第一次选择最近的顶点为起点自身，并更新相邻未确认顶点的距离

![](https://upload-images.jianshu.io/upload_images/9738807-87440317015fb084.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

***step 2：***

![](https://upload-images.jianshu.io/upload_images/9738807-c65dae2ad7204ae8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

***step 3：***

![](https://upload-images.jianshu.io/upload_images/9738807-05785e37e51bb599.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

***step 4：***

![](https://upload-images.jianshu.io/upload_images/9738807-fbabd8e3f7f6ad4c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

***step 5：***

![](https://upload-images.jianshu.io/upload_images/9738807-15ae9d60ff499202.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

***step 6：***

![](https://upload-images.jianshu.io/upload_images/9738807-305230667ea8b934.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

***step 7：***

![](https://upload-images.jianshu.io/upload_images/9738807-10f45a285858bc2f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

***step 8：***

![](https://upload-images.jianshu.io/upload_images/9738807-ee25fe6e4b3bd653.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

***step 9：***

![](https://upload-images.jianshu.io/upload_images/9738807-32359df6c14078f3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 算法示例

1. ```Dijkstra``` 算法示例

```
def dijkstra(graph, start):
    vertices, verticesIndex = [{'index': i, 'weight': None} for i in range(graph.number)], [i for i in range(graph.number)]
    vertices[start - 1]['weight'] = 0
    heapSort(vertices, verticesIndex)
    while len(vertices) > 0:
        swapVertices(vertices, verticesIndex, 0, -1)
        vertex = vertices.pop()
        transformToHeap(vertices, verticesIndex, 0, len(vertices))
        updateDistance(graph, vertices, verticesIndex, vertex)
```

这里使用 ```vertices``` 列表存储每个顶点元素，每个元素包括两个属性，```index``` 为顶点下标，```weight``` 为顶点距离起点的大小。算法中使用 ```verticesIndex``` 列表存储每个顶点元素在 ```vertices``` 列表中的下标位置。使用 ```heapSort``` 堆排序对每个顶点到起点的距离进行排序，即对 ```vertices``` 列表进行排序。使用 ```swapVertices``` 函数将 ```vertices``` 列表首尾元素交换，将最小元素放置在列表尾部并执行出栈操作，使用 ```transformToHeap``` 函数调整 ```vertices``` 列表为小顶堆，然后调用 ```updateDistance``` 函数完成对相邻顶点的距离更新。

2. 交换列表首尾元素

```
def swapVertices(vertices, verticesIndex, origin, target):
    vertices[origin], vertices[target] = vertices[target], vertices[origin]
    verticesIndex[vertices[origin]['index']], verticesIndex[vertices[target]['index']] = origin, target
```

当 ```vertices``` 列表调整为小顶堆之后，将列表首、尾元素交换，则列表尾元素即为距离起点最近的顶点元素。

3. 将列表尾部顶点元素出栈后，更新该顶点的相邻未确认顶点距离起点的权值

```
def updateDistance(graph, vertices, verticesIndex, agent):
    node = graph.list[agent['index']]
    while node:
        if verticesIndex[node.index - 1] == -1:  # whether the node in sub graph
            node = node.next
            continue
        vertex = vertices[verticesIndex[node.index - 1]]
        if not vertex['weight'] or vertex['weight'] > agent['weight'] + node.weight:
            vertex['weight'] = agent['weight'] + node.weight
            pos = verticesIndex[vertex['index']]
            while pos > 0 and (not vertices[(pos - 1) // 2]['weight'] or vertices[pos]['weight'] < vertices[(pos - 1) // 2]['weight']):
                swapVertices(vertices, verticesIndex, pos, (pos - 1) // 2)
                pos = (pos - 1) // 2
        node = node.next
```
对每一个相邻顶点，若属于未确认顶点，则判断是否更新到起点的距离。更新距离后的 ```while``` 循环操作，目的为调整堆结构为小顶堆。

> ```Dijkstra``` 算法及算法中调用的函数都与 ```prim``` 算法较大相像，可以参考[最小生成树](https://www.jianshu.com/p/cf21443b3838)中 ```prim``` 算法的部分作辅助理解。

### 性能分析

```dijkstra``` 算法中构造顶点列表的时间复杂度为 $O(|V|)$。使用堆排序对顶点列表进行排序，时间复杂度为 $O(|V|log |V|)$。```dijkstra``` 算法中 ```while``` 循环取权值最小顶点元素，并调整元素取出后列表的堆结构，所以调整复杂度为 $O(|V|log |V|)$；同时，循环结构内执行 ```updateDistance``` 函数，更新每个取出顶点的相邻顶点权值，所以更新顶点数为 $O(|E|)$，因为每个顶点更新距离后，需要调整堆结构为小顶堆，所以更新复杂度为 $O(|E|log |V|)$。所以```prim``` 算法的总时间复杂度为 $O(|E|log |V|)$。

### 代码附录

[Dijkstra算法代码及测试结果](./dijkstra.py)