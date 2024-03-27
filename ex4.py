import timeit

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

    def removeNode(self, node):
        for k, v in self.nodes.pop(node.data).edges.items():
            k.edges.pop(node)

    def addEdge(self, node1, node2, weight):
        node1.edges[node2] = weight
        node2.edges[node1] = weight

    def removeEdge(self, node1, node2):
        node1.edges.pop(node2)
        node2.edges.pop(node1)

    def dfs(self, start):
        visited = set()
        dfs_order = []

        def dfs_util(node):
            visited.add(node)
            dfs_order.append(node.value)
            for neighbour in node.edges:
                if neighbour not in visited:
                    dfs_util(neighbour)

        dfs_util(self.nodes[start])
        return dfs_order


class Graph2:
    def __init__(self, num_nodes):
        self.nodes = {}
        self.matrix = [[0]*num_nodes for _ in range(num_nodes)]
        self.node_to_index = {}  # new dictionary to map node values to indices
        self.index = 0  # counter for the next index

    def addNode(self, data):
        if data not in self.nodes:
            self.nodes[data] = GraphNode(data)
            self.node_to_index[data] = self.index
            self.index += 1
        return self.nodes[data]

    def addEdge(self, node1, node2, weight):
        index1 = self.node_to_index[node1.value]
        index2 = self.node_to_index[node2.value]
        self.matrix[index1][index2] = weight
        self.matrix[index2][index1] = weight

    def dfs(self, start):
        visited = [False] * len(self.nodes)
        dfs_order = []

        def dfs_util(v):
            visited[v] = True
            dfs_order.append(v)
            for i, weight in enumerate(self.matrix[v]):
                if weight != 0 and not visited[i]:
                    dfs_util(i)

        dfs_util(start)
        return dfs_order


def importFromFile(file):
    unique_nodes = set()
    with open(file, 'r') as f:
        for line in f:
            if '--' in line:
                nodes = line.split('--')
                unique_nodes.add(int(nodes[0].strip()))
                unique_nodes.add(int(nodes[1].split('[')[0].strip()))

    num_nodes = len(unique_nodes)
    graph = Graph()
    graph2 = Graph2(num_nodes)

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
                weight = int(line[3].removeprefix('[weight=').removesuffix(']'))
                graph.addEdge(node1, node2, weight)
                node1_2 = graph2.addNode(int(line[0]))
                node2_2 = graph2.addNode(int(line[2]))
                graph2.addEdge(node1_2, node2_2, weight)

    return graph, graph2


graph, graph2 = importFromFile('random.dot')

# Measure the performance of dfs() method
times_graph = timeit.repeat(lambda: graph.dfs('0'), repeat=10, number=1)
times_graph2 = timeit.repeat(lambda: graph2.dfs(0), repeat=10, number=1)

print(f"Graph: max={max(times_graph)}, min={min(times_graph)}, avg={sum(times_graph)/len(times_graph)}")
print(f"Graph2: max={max(times_graph2)}, min={min(times_graph2)}, avg={sum(times_graph2)/len(times_graph2)}")

# Discussion of results:
# Based on the results, the maximum, minimum, and average times for Graph are lower than those of Graph2. and
# thus, the Graph class performs the DFS faster than the Graph2 class. It is important to note that
# Graph utilizes an adjacency list representation while Graph2 uses an adjacency matrix representation. 
# This is because adjacency lists are more space-efficient for sparce graphs, and can be more time efficient
# for operations such as iterating the neighbours of a node. However, adjacenty matrices can be more efficient 
# for dense graphs, where pairs of nodes are connected. An operation such as checking whether an edge exists
# between two nodes are better handles by adjecency matrices.

