from adjacencyList import AdjacencyList
from adjacencyList import Edge


# get edges from adjacency list
def getEdgesFromAdjacencyList(graph):
    edges = []
    for i in range(graph.number):
        node = graph.list[i]
        while node:
            edge, node = Edge(i + 1, node.index, node.weight), node.next
            edges.append(edge)
    return edges


# update distance between source and the end vertex
def releax(edge, distance, parent):
    if distance[edge.begin - 1] == None:
        pass
    elif distance[edge.end - 1] == None or distance[edge.end - 1] > distance[edge.begin - 1] + edge.weight:
        distance[edge.end - 1] = distance[edge.begin - 1] + edge.weight
        parent[edge.end - 1] = edge.begin - 1
        return True
    return False


# representing shortest path
def bellman_ford(graph, start, end):
    distance, parent = [None for i in range(graph.number)], [None for i in range(graph.number)]
    times, distance[start - 1], edges = 1, 0, getEdgesFromAdjacencyList(graph)
    flag = True
    while flag and times < graph.number:
        flag = False
        for i in range(len(edges)):
            if releax(edges[i], distance, parent) and not flag:
                flag = True
        times += 1
    for i in range(len(edges)):
        if releax(edges[i], distance, parent):
            return False
    return True


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
    bellman_ford(graph, 2, 6)
