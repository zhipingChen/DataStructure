from adjacencyList import AdjacencyList
from adjacencyList import heapSort
from adjacencyList import transformToHeap

# update the distance of vertices
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
            while pos > 0 and (
                        not vertices[(pos - 1) // 2]['weight'] or vertices[pos]['weight'] < vertices[(pos - 1) // 2][
                        'weight']):
                swapVertices(vertices, verticesIndex, pos, (pos - 1) // 2)
                pos = (pos - 1) // 2
        node = node.next

# swap two vertex
def swapVertices(vertices, verticesIndex, origin, target):
    vertices[origin], vertices[target] = vertices[target], vertices[origin]
    verticesIndex[vertices[origin]['index']], verticesIndex[vertices[target]['index']] = origin, target

# representing shortest path
def dijkstra(graph, start):
    vertices, verticesIndex = [{'index': i, 'weight': None} for i in range(graph.number)], [i for i in
                                                                                            range(graph.number)]
    vertices[start - 1]['weight'] = 0
    heapSort(vertices, verticesIndex)
    while len(vertices) > 0:
        swapVertices(vertices, verticesIndex, 0, -1)
        vertex = vertices.pop()
        transformToHeap(vertices, verticesIndex, 0, len(vertices))
        updateDistance(graph, vertices, verticesIndex, vertex)
        print('index:',vertex['index']+1,'weight:',vertex['weight'])


if __name__ == '__main__':
    graph = AdjacencyList(9)
    graph.insert(1, 2, 4)
    graph.insert(1, 8, 8)
    graph.insert(2, 1, 4)
    graph.insert(2, 3, 8)
    graph.insert(2, 8, 11)
    graph.insert(3, 2, 8)
    graph.insert(3, 4, 7)
    graph.insert(3, 6, 4)
    graph.insert(3, 9, 2)
    graph.insert(4, 3, 7)
    graph.insert(4, 5, 9)
    graph.insert(4, 6, 14)
    graph.insert(5, 4, 9)
    graph.insert(5, 6, 10)
    graph.insert(6, 3, 4)
    graph.insert(6, 4, 14)
    graph.insert(6, 5, 10)
    graph.insert(6, 7, 2)
    graph.insert(7, 6, 2)
    graph.insert(7, 8, 1)
    graph.insert(7, 9, 6)
    graph.insert(8, 1, 8)
    graph.insert(8, 2, 11)
    graph.insert(8, 7, 1)
    graph.insert(8, 9, 7)
    graph.insert(9, 3, 2)
    graph.insert(9, 7, 6)
    graph.insert(9, 8, 7)
    dijkstra(graph, 1)