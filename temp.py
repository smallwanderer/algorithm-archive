class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

class GreedyKruskal:
    def kruskal(self, n, edges):
        edges.sort()
        
        disjoint_set = DisjointSet(n)
        mst_weight = 0

        for weight, u, v in edges:
            if disjoint_set.find(u) != disjoint_set.find(v):
                disjoint_set.union(u, v)
                mst_weight += weight
        
        return mst_weight


import sys
input = sys.stdin.readline

V, E = map(int, input().strip().split())
edges = []

for _ in range(E):
    u, v, weight = map(int, input().strip().split())
    edges.append((weight, u - 1, v - 1))
    
kruskal = GreedyKruskal()
mst_weight = kruskal.kruskal(V, edges)
print(mst_weight)