"""
Watering the Fields problem
Algoritm: MST
문제 링크: https://www.acmicpc.net/problem/10021
"""

import sys
input = sys.stdin.readline

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
                self.parent[root_u] = root_v
                self.rank[root_u] += 1

import math
def watering_the_fields():
    N, C = map(int, input().split())
    M = 2000

    points = [tuple(map(int, input().split())) for _ in range(N)]

    # Edges를 계산하기 위해 C이상의 N!개의 모든 edges를 구해야 하는것인가?
    edges = []
    for x, y in points:
        for u, v in points:
            weight = math.pow(abs(u-x), 2) + math.pow(abs(v-y), 2)
            if weight >= C:
                edges.append((weight, x*M+y, u*M+v))

    # 시작 정점이 정해지지 않았으므로 Kruskal 알고리즘 사용
    edges.sort()

    disjoint = DisjointSet(N)
    mst_weight = 0
    edges_cnt = 0

    for weight, u, v in edges:
        if disjoint.find(u) != disjoint.find(v):
            disjoint.union(u, v)
            mst_weight += weight
            edges_cnt += 1
    
    # print(edges_cnt)
    return mst_weight if edges_cnt == N-1 else -1


import heapq
def prim_watering_the_fields():
    N, C = map(int, input().split())
    points = [tuple(map(int, input().split())) for _ in range(N)]

    visited = {point:False for point in points}
    min_heap = [(0, points[0])]

    mst_weight = 0
    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue    
        visited[u] = True
        mst_weight += weight

        for p in points:
            if not visited[p]:
                weight = math.pow(abs(p[0]-u[0]),2) + \
                math.pow(abs(p[1]-u[1]), 2)
                if weight >= C:
                    heapq.heappush(min_heap, (weight, p))
        
    return mst_weight if all(visited.values()) else -1

import sys
input = sys.stdin.readline

def list_prim_watering_the_fields(start=0):
    N, C = map(int, input().split())
    points = [tuple(map(int, input().split())) for _ in range(N)]

    INF = float('inf')
    distance = [INF] * N
    visited = [False] * N

    distance[0] = 0
    mst_weight = 0
    for _ in range(N):
        current, best = -1, INF
        for i in range(N):
            if not visited[i] and distance[i] < best:
                current, best = i, distance[i]
        
        # 종료조건: 더이상 current가 갱신되지 않았음
        if current == -1:
            return -1
        
        # MST에 현재노드 추가
        visited[current] = True
        mst_weight += best

        # 거리 갱신: currnet를 기준으로 모든 미방문 접점들에 대해 최소 weight 갱신
        for j in range(N):
            if not visited[j]:
                x, y = points[current]
                u, v = points[j]
                a, b = abs(x-u), abs(y-v)
                weight = a*a + b*b
                if weight >= C:
                    distance[j] = min(distance[j], weight)
        
    return mst_weight

result = list_prim_watering_the_fields()
print(result)
    
    
    

