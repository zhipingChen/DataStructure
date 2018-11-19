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