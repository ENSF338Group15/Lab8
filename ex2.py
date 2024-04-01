#1. a) The slow aproach to implement this queue to with linear search on a list of the nodes to find the node with the smallest distance
#   b) The fast aproach to implement this queue is with a binary heap to maintain functionality of the priority queue.
import timeit
import heapq

class GraphNode:
    def __init__(self, value):
        self.value = value
        self.edges = {}


class Graph:
    def __init__(self):
        self.nodes = {}

    def addNode(self, data):
        if data in self.nodes:
            return self.nodes[data]
        node = GraphNode(data)
        self.nodes[data] = node
        return node

    def addEdge(self, node1, node2, weight):
        node1.edges[node2] = weight
        node2.edges[node1] = weight

    def slowSP(self, start_node):
        distances = {node: float('inf') for node in self.nodes.values()}
        distances[start_node] = 0
        visited = set()

        while len(visited) < len(self.nodes):
            min_distance = float('inf')
            min_node = None

            for node in self.nodes.values():
                if node not in visited and distances[node] < min_distance:
                    min_distance = distances[node]
                    min_node = node

            visited.add(min_node)

            for neighbor, weight in min_node.edges.items():
                if distances[min_node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[min_node] + weight

        return distances

    def fastSP(self, start_node):
        distances = {node: float('inf') for node in self.nodes.values()}
        distances[start_node] = 0
        visited = set()
        min_heap = [(0, start_node)]

        while min_heap:
            distance, node = heapq.heappop(min_heap)

            if node in visited:
                continue

            visited.add(node)

            for neighbor, weight in node.edges.items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    heapq.heappush(min_heap, (distances[neighbor], neighbor))

        return distances
