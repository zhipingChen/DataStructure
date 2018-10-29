# tree node definition
class Node(object):
    def __init__(self, value, content=None, lchild=None, rchild=None):
        self.lchild = lchild
        self.rchild = rchild
        self.value = value
        self.content = content

# tree definition
class Tree(object):
    def __init__(self, root=None):
        self.root = root
        self.codeMap = {}

    # initialize the huffman tree code map
    def initializeCodeMap(self):
        initializeCodeMap(self.root, [], self.codeMap)

    # encode
    def encode(self, chars):
        bytes = ''
        for i in chars:  # get the mapped bytes
            bytes += self.codeMap.get(i.upper(), '###')
        return bytes

    # decode
    def decode(self, bytes):
        chars = ''
        tmpNode = self.root
        for i in bytes:
            if i == '0':
                tmpNode = tmpNode.lchild
            elif i == '1':
                tmpNode = tmpNode.rchild
            if not tmpNode.lchild:
                chars += tmpNode.content
                tmpNode = self.root
        return chars

    # merge two nodes and return one root node
    def acceptNewNode(self, value, content):
        if not self.root:
            self.root = Node(value, content)
        else:
            newNode = Node(value, content)
            newRoot = Node(self.root.value + value)
            lchild, rchild = (self.root, newNode) if self.root.value < value else (newNode, self.root)
            newRoot.lchild, newRoot.rchild = lchild, rchild
            self.root = newRoot

# initialize the huffman tree code map
def initializeCodeMap(node, byteArr, codeMap):
    if node.lchild:
        byteArr.append('0')
        initializeCodeMap(node.lchild, byteArr, codeMap)
        byteArr.append('1')
        initializeCodeMap(node.rchild, byteArr, codeMap)
        byteArr.pop() if len(byteArr) > 0 else None  # in case only the root node left
    else:
        codeMap[node.content] = ''.join(byteArr)
        byteArr.pop()

# construct the huffman tree
def createHuffmanTree(valueArr, contentArr):
    insertionSort(valueArr, contentArr)  # synchronise sort the valueArr and contentArr
    hfTree = Tree()
    for i in range(len(valueArr)):  # construct the huffman tree
        hfTree.acceptNewNode(valueArr[i], contentArr[i])
    hfTree.initializeCodeMap() # initialize the huffman tree code map
    return hfTree

# synchronise sort the valueArr and contentArr
def insertionSort(valueArr, contentArr):
    for i in range(1, len(valueArr)):  # iteration times
        tmpValue = valueArr[i]
        tmpContent = contentArr[i]
        while i > 0 and tmpValue < valueArr[i - 1]:
            valueArr[i] = valueArr[i - 1]
            contentArr[i] = contentArr[i - 1]
            i = i - 1
        valueArr[i] = tmpValue
        contentArr[i] = tmpContent


if __name__ == '__main__':
    valueArr = [5, 3, 4, 0, 2, 1, 8, 6, 9, 7]
    contentArr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    huTree = createHuffmanTree(valueArr, contentArr)
    chars = 'hIebAhcHdfGc'
    bytes = huTree.encode(chars)
    print(chars.lower(), 'encode =', bytes)

    chars = huTree.decode(bytes)
    print(bytes, 'decode =', chars.lower())