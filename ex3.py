class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True  

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def mst(self):
        self.edges.sort(key=lambda edge: edge[2])
        mst_edges = []
        union_find = UnionFind(self.vertices)

        for edge in self.edges:
            u, v, weight = edge
            if union_find.union(u, v):
                mst_edges.append(edge)

        mst_graph = Graph(self.vertices)
        mst_graph.edges = mst_edges
        return mst_graph

graph = Graph(5)
graph.add_edge(0, 3, 3)
graph.add_edge(0, 4, 12)
graph.add_edge(3, 1, 5)
graph.add_edge(3, 2, 3)
graph.add_edge(4, 2, 7)
graph.add_edge(1, 2, 2)

mst_graph = graph.mst()

print("Minimum Spanning Tree Edges:")
for edge in mst_graph.edges:
    print(edge)
    
# Used ChatGPT for UnionFind class