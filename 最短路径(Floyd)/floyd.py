from adjacencyMatrix import AdjacencyMatrix

# representing shortest path for each vertex
def floyd(graph):
    matrix = graph.list
    for k in range(graph.number):
        for i in range(graph.number-1,-1,-1):
            for j in range(graph.number):
                if matrix[i][k] != None and matrix[k][j] != None and (matrix[i][j] == None or matrix[i][k] + matrix[k][j] < matrix[i][j]):
                    matrix[i][j] = matrix[i][k] + matrix[k][j]

def show(graph):
    for i in range(graph.number):
        print('node', (i + 1), 'distance:', end = ' ')
        j = 0
        while j < graph.number:
            print(graph.list[i][j], end = ' ')
            j += 1
        print()

if __name__ == '__main__':
    graph = AdjacencyMatrix(9)
    graph.insert(1, 1, 0)
    graph.insert(1, 2, 4)
    graph.insert(1, 8, 8)
    graph.insert(2, 1, 4)
    graph.insert(2, 2, 0)
    graph.insert(2, 3, 8)
    graph.insert(2, 8, 11)
    graph.insert(3, 2, 8)
    graph.insert(3, 3, 0)
    graph.insert(3, 4, 7)
    graph.insert(3, 6, 4)
    graph.insert(3, 9, 2)
    graph.insert(4, 3, 7)
    graph.insert(4, 4, 0)
    graph.insert(4, 5, 9)
    graph.insert(4, 6, 14)
    graph.insert(5, 4, 9)
    graph.insert(5, 5, 0)
    graph.insert(5, 6, 10)
    graph.insert(6, 3, 4)
    graph.insert(6, 4, 14)
    graph.insert(6, 5, 10)
    graph.insert(6, 6, 0)
    graph.insert(6, 7, 2)
    graph.insert(7, 6, 2)
    graph.insert(7, 7, 0)
    graph.insert(7, 8, 1)
    graph.insert(7, 9, 6)
    graph.insert(8, 1, 8)
    graph.insert(8, 2, 11)
    graph.insert(8, 7, 1)
    graph.insert(8, 8, 0)
    graph.insert(8, 9, 7)
    graph.insert(9, 3, 2)
    graph.insert(9, 7, 6)
    graph.insert(9, 8, 7)
    graph.insert(9, 9, 0)
    floyd(graph)
    show(graph)