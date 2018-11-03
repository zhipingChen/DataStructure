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

# graph edge definition
class Edge(object):
    def __init__(self, begin, end, weight):
        self.begin = begin
        self.end = end
        self.weight = weight

# use the quick sort
def sort(edges, left, right):
    if left < right:
        divide = quickSort(edges, left, right)
        sort(edges, left, divide - 1)
        sort(edges, divide + 1, right)

def quickSort(edges, left, right):
    index, middleValue = left, edges[right]
    for i in range(left, right):
        if edges[i].weight > middleValue.weight:
            if i != index:
                edges[i], edges[index] = edges[index], edges[i]
            index += 1
    if right != index:
        edges[right], edges[index] = edges[index], edges[right]
    return index

# use the heap sort
def heapSort(vertices, verticesIndex):
    index = len(vertices) // 2 - 1
    while index >= 0:
        transformToHeap(vertices, verticesIndex, index, len(vertices))
        index = index - 1

def transformToHeap(vertices, verticesIndex, index, end):
    targetIndex, leftChildIndex, rightChildIndex = index, 2 * index + 1, 2 * index + 2
    if leftChildIndex < end and vertices[leftChildIndex]['weight'] != None:
        if not vertices[targetIndex]['weight'] or (vertices[leftChildIndex]['weight'] < vertices[targetIndex]['weight']):
            targetIndex = leftChildIndex
    if rightChildIndex < end and vertices[rightChildIndex]['weight'] != None:
        if not vertices[targetIndex]['weight'] or (vertices[rightChildIndex]['weight'] < vertices[targetIndex]['weight']):
            targetIndex = rightChildIndex
    if not targetIndex == index:
        vertices[index], vertices[targetIndex] = vertices[targetIndex], vertices[index]
        verticesIndex[vertices[targetIndex]['index']], verticesIndex[vertices[index]['index']] = targetIndex, index
        transformToHeap(vertices, verticesIndex, targetIndex, end)