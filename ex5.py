"""
1. DFS searches a branch until it completely explored one part of the tree, and then moves data, so it can be used for topological sorting.
"""


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

    def isdag(self):
        visited = set()
        recStack = set()

        for node in self.nodes.values():
            if node not in visited:
                if self.dfs_cycle_check(node, visited, recStack):
                    return False
        return True

    def dfs_cycle_check(self, node, visited, recStack):
        visited.add(node)
        recStack.add(node)
        for neighbor in node.edges:
            if neighbor not in visited:
                if self.dfs_cycle_check(neighbor, visited, recStack):
                    return True
            elif neighbor in recStack:
                return True
        recStack.remove(node)
        return False

    def toposort(self):
        if not self.isdag():
            return None

        visited = set()
        stack = []

        for node in self.nodes.values():
            if node not in visited:
                self.dfs_toposort(node, visited, stack)

        return [node.value for node in reversed(stack)]

    def dfs_toposort(self, node, visited, stack):
        visited.add(node)
        for neighbor in node.edges:
            if neighbor not in visited:
                self.dfs_toposort(neighbor, visited, stack)
        stack.append(node)
