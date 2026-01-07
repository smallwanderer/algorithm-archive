from typing import List, Tuple
import heapq

"""
Minimum Spanning Tree (MST) Implementations
- Kruskal's Algorithm : greedy/Kruskal.py에서 확인 가능
- Prim's Algorithm: greedy/Prim.py에서 확인 가능
"""

class UnionFind:
    """Union-Find (Disjoint Set Union) for Kruskal's Algorithm"""
    
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x: int) -> int:
        """Find the root parent of x"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> bool:
        """Union two sets. Return True if successful"""
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        
        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        
        return True


def kruskal(n: int, edges: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
    """
    Kruskal's Algorithm - O(E log E)
    
    Args:
        n: number of vertices
        edges: list of (weight, u, v)
    
    Returns:
        MST edges
    """
    edges.sort()
    uf = UnionFind(n)
    mst = []
    
    for weight, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            if len(mst) == n - 1:
                break
    
    return mst


def prim(n: int, graph: List[List[Tuple[int, int]]]) -> List[Tuple[int, int, int]]:
    """
    Prim's Algorithm - O(E log V)
    
    Args:
        n: number of vertices
        graph: adjacency list [(neighbor, weight), ...]
    
    Returns:
        MST edges
    """
    
    visited = [False] * n
    min_heap = [(0, 0)]  # (weight, vertex)
    mst = []
    
    while min_heap:
        weight, u = heapq.heappop(min_heap)
        
        if visited[u]:
            continue
        
        visited[u] = True
        
        if weight > 0:  # Skip root edge
            mst.append((u, weight))
        
        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))
    
    return mst


# Example usage
if __name__ == "__main__":
    # Test Kruskal
    edges = [
        (1, 0, 1),
        (3, 0, 3),
        (4, 1, 2),
        (2, 1, 3),
        (5, 2, 3),
    ]
    print("Kruskal MST:", kruskal(4, edges))
    
    # Test Prim
    graph = [
        [(1, 1), (3, 3)],
        [(0, 1), (2, 4), (3, 2)],
        [(1, 4), (3, 5)],
        [(0, 3), (1, 2), (2, 5)],
    ]
    print("Prim MST:", prim(4, graph))