from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, adj, visited, mark):
    q = deque([start])
    visited[start] = mark
    cnt = 1
    while q:
        u = q.popleft()
        for v in adj[u]:
            if visited[v] != mark:
                visited[v] = mark
                q.append(v)
                cnt += 1
    return cnt

n, m = map(int, input().split())
g = [[] for _ in range(n)]
rg = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    g[a].append(b)
    rg[b].append(a)

visited = [0] * n
mark = 1
ans = 0
for i in range(n):
    f = bfs(i, g, visited, mark); mark += 1
    b = bfs(i, rg, visited, mark); mark += 1
    if f + b - 1 == n:
        ans += 1

print(ans)