"""
Kruskal's Algorithm for Minimum Spanning Tree (MST)

Kruskal 알고리즘은 그래프에서 최소 신장 트리를 찾기 위한 그리디 알고리즘입니다.
"""

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
        """Kruskal 알고리즘은 Minimum Spanning Tree (MST)을 찾기 위한 알고리즘입니다.

        Args:
            n (int): 그래프의 노드 수.
            edges (List[Tuple[int, int, int]]): 간선 리스트 (가중치, 시작 노드, 끝 노드).

        Returns:
            Tuple[int, List[Tuple[int, int, int]]]: MST의 총 가중치와 MST에 포함된 간선 리스트.
        """
        # Sort edges based on their weights
        edges.sort()
        
        disjoint_set = DisjointSet(n)
        mst_weight = 0
        mst_edges = []

        for weight, u, v in edges:
            if disjoint_set.find(u) != disjoint_set.find(v):
                disjoint_set.union(u, v)
                mst_weight += weight
                mst_edges.append([u, v])
        
        return mst_weight, mst_edges


# 테스트 예시
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    V, E = map(int, input().strip().split())
    edges = []

    for _ in range(E):
        u, v, weight = map(int, input().strip().split())
        edges.append((weight, u - 1, v - 1))  # 0-indexed 
    
    kruskal = GreedyKruskal()
    mst_weight, mst_edges = kruskal.kruskal(V, edges)
    print("MST Weight:", mst_weight)
    print("MST Edges:", mst_edges)