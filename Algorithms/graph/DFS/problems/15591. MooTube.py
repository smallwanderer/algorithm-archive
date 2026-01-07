"""
문제 링크 : https://www.acmicpc.net/problem/15591
Algoritm: DFS
"""

import sys
input = sys.stdin.readline

def dfs_mootube():
    N, Q = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(N - 1):
        a, b, w = map(int, input().split())
        graph[a].append((b, w))
        graph[b].append((a, w))
    
    for _ in range(Q):
        k, v = map(int, input().split())
        visited = [False] * (N + 1)
        stack = [v]
        visited[v] = True
        count = 0

        while stack:
            current = stack.pop()
            for neighbor, weight in graph[current]:
                if not visited[neighbor] and weight >= k:
                    visited[neighbor] = True
                    stack.append(neighbor)
                    count += 1
        
        print(count)

if __name__ == "__main__":
    dfs_mootube()