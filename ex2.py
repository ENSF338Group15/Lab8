import heapq
import timeit
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, node1, node2, distance):
        if node1 not in self.edges:
            self.edges[node1] = {}
        if node2 not in self.edges:
            self.edges[node2] = {}
        self.edges[node1][node2] = distance
        self.edges[node2][node1] = distance

# this version of the algorithm takes a long time to exectue
    def slowSP(self, source):
        distances = {node: float('infinity') for node in self.nodes}
        distances[source] = 0
        queue = list(self.nodes)

        while queue:
            min_node = None
            for node in queue:
                if min_node is None or distances[node] < distances[min_node]:
                    min_node = node

            queue.remove(min_node)

            for neighbor in self.edges[min_node]:
                alt_distance = distances[min_node] + self.edges[min_node][neighbor]
                if alt_distance < distances[neighbor]:
                    distances[neighbor] = alt_distance

        return distances

    def fastSP(self, source):
        distances = {node: float('infinity') for node in self.nodes}
        distances[source] = 0
        queue = [(0, source)]

        while queue:
            curr_distance, min_node = heapq.heappop(queue)

            for neighbor in self.edges[min_node]:
                alt_distance = curr_distance + self.edges[min_node][neighbor]
                if alt_distance < distances[neighbor]:
                    distances[neighbor] = alt_distance
                    heapq.heappush(queue, (alt_distance, neighbor))

        return distances

def importFromFile(file):
    graph = Graph()

    with open(file, 'r') as f:
        for line in f:
            if '--' in line:  # We're only interested in lines that represent edges
                line = line.strip().removesuffix(';')
                node1, rest = line.split('--')
                node2, weight = rest.split('[weight=')
                node2 = node2.strip()
                weight = int(weight.removesuffix(']'))

                graph.add_node(node1)
                graph.add_node(node2)
                graph.add_edge(node1, node2, weight)

    return graph

# Import the graph from the random.dot file
graph = importFromFile('random.dot')

# Measure the performance of slowSP(node)
slow_times = []
for node in graph.nodes:
    start_time = timeit.default_timer()
    graph.slowSP(node)
    end_time = timeit.default_timer()
    slow_times.append(end_time - start_time)

# Measure the performance of fastSP(node)
fast_times = []
for node in graph.nodes:
    start_time = timeit.default_timer()
    graph.fastSP(node)
    end_time = timeit.default_timer()
    fast_times.append(end_time - start_time)

# Report average, max and min time
print(f"slowSP(node): max={max(slow_times)}, min={min(slow_times)}, avg={sum(slow_times)/len(slow_times)}")
print(f"fastSP(node): max={max(fast_times)}, min={min(fast_times)}, avg={sum(fast_times)/len(fast_times)}")

# Plot a histogram of the distribution of execution times
plt.hist(slow_times, bins=20, alpha=0.5, label='slowSP(node)')
plt.hist(fast_times, bins=20, alpha=0.5, label='fastSP(node)')
plt.xlabel('Execution time')
plt.ylabel('Number of nodes')
plt.legend(loc='upper right')
plt.show()

# Answer to question 4:
# From the graph, the fastSP(node) method is able to handle a greater number of nodes with faster
# execution times than the slopwSP(node) method.

# the inneficient way to implement the Dijkstra's algorithm is to use an array to use
# as the queue, this way would scan the enture list to find the node with the smallest distance. This
# has a time complecity of O(n), n being the number of nodes in the graph. 

# The efficient way to implement the Dijkstra's algorithm is to use a priority queue or a min-heap, 
# this type of data structure efficeinty finds and removes the smallest element. The time complexity of 
# this operation is O(log n)

 

