"""
Prim's Algorithm Implementation

Prim 알고리즘은 그래프에서 최소 신장 트리를 찾기 위한 그리디 알고리즘입니다.
"""

import heapq

class GreedyPrim:
    def prim(self, n, edges, start=0):
        """Prim 알고리즘은 Minimum Spanning Tree (MST)을 찾기 위한 알고리즘입니다.

        Args:
            n (int): 그래프의 노드 수.
            edges (List[List[Tuple[int, int]]]): 인접 리스트 형태의 그래프 표현 (노드, 가중치).
            start (int, optional): 시작 노드. 기본값은 0.

        Returns:
            int: MST의 총 가중치.
        """
        visited = [False] * n
        min_heap = [(0, start)]  # (가중치, 노드)

        mst_weight = 0
        while min_heap:
            weight, u = heapq.heappop(min_heap)
            if visited[u]:
                continue
            visited[u] = True
            mst_weight += weight

            for v, w in edges[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (w, v))
            
        return mst_weight

# 테스트 예시
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    V, E = map(int, input().strip().split())
    edges = [[] for _ in range(V)]

    for _ in range(E):
        u, v, weight = map(int, input().strip().split())
        edges[u - 1].append((v - 1, weight))
        edges[v - 1].append((u - 1, weight))

    prim = GreedyPrim()
    mst_weight = prim.prim(V, edges)
    print(mst_weight)
            