class GraphNode:
    def __init__(self, value):
        self.value = value
        self.edges = {}


class Graph:
    def __init__(self):
        self.nodes = {}

    def addNode(self, data):
        if data in self.nodes.keys():
            return self.nodes[data]
        node = GraphNode(data)
        self.nodes[data] = node
        return node

    # Not sure if implement is correct
    def removeNode(self, node):
        for k, v in self.nodes.pop(node.data).edges.items():
            k.edges.pop(node)

    def addEdge(self, node1, node2, weight):
        node1.edges[node2] = weight
        node2.edges[node1] = weight

    def removeEdge(self, node1, node2):
        node1.edges.pop(node2)
        node2.edges.pop(node1)


def importFromFile(file):
    graph = Graph()
    with open(file, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            if '--' not in line:
                continue
            line = line.strip()
            line = line.removesuffix(';')
            line = line.split(' ')
            line.extend(line.pop(2).split('\t'))
            node1 = graph.addNode(line[0])
            node2 = graph.addNode(line[2])
            if len(line) > 2:
                graph.addEdge(node1, node2, line[3].removeprefix('[weight=').removesuffix(']'))


importFromFile('random.dot')
