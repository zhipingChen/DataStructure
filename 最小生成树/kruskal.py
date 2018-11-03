from adjacencyList import AdjacencyList
from adjacencyList import Edge
from adjacencyList import sort

# get edges from adjacency list
def getEdgesFromAdjacencyList(graph):
    edges = []
    for i in range(graph.number):
        node = graph.list[i]
        while node:
            edge, node = Edge(i + 1, node.index, node.weight), node.next
            edges.append(edge)
    return edges


# get the origin vertex of the sub graph
def origin(vertices, index):
    while vertices[index] != index:
        index = vertices[index]
    return index


# generate the minimum spanning tree
def kruskal(graph):
    edges, vertices = getEdgesFromAdjacencyList(graph), [i for i in range(graph.number)]
    sort(edges, 0, len(edges) - 1)
    weightSum, edgeNumber = 0, 0
    while edgeNumber < graph.number - 1:
        edge = edges.pop()
        beginOrigin, endOrigin = origin(vertices, edge.begin - 1), origin(vertices, edge.end - 1)
        if (beginOrigin != endOrigin): # whether the two vertices belong to same graph
            vertices[beginOrigin] = endOrigin  # identify the two vertices in the same sub graph
            weightSum, edgeNumber = weightSum + edge.weight, edgeNumber + 1  # calculate the total edge weight and edge number

if __name__ == '__main__':
    graph = AdjacencyList(9)
    graph.insert(1, 2, 4)
    graph.insert(1, 8, 8)
    graph.insert(2, 3, 8)
    graph.insert(2, 8, 11)
    graph.insert(3, 4, 7)
    graph.insert(3, 6, 4)
    graph.insert(3, 9, 2)
    graph.insert(4, 5, 9)
    graph.insert(4, 6, 14)
    graph.insert(5, 6, 10)
    graph.insert(6, 7, 2)
    graph.insert(7, 8, 1)
    graph.insert(7, 9, 6)
    graph.insert(8, 9, 7)
    kruskal(graph)