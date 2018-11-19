# adjacency list definition
class AdjacencyMatrix(object):
    def __init__(self, number):
        self.number = number
        self.list = [[None] * number for i in range(number)]

    # insert node
    def insert(self, origin, index, weight = 1):
        self.list[origin - 1][index - 1] = weight

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