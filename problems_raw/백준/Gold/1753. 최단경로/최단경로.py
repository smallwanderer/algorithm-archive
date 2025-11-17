# 백준 1753 : 최단경로
# 다이크스트라 알고리즘 이용

import heapq

class Dijkstra:
  def __init__(self, n, v):
    self.node = n
    self.vertex = v

  def dijkstra(self, st):
    dist = [float("inf")] * self.node
    dist[st] = 0
    hq = [(0, st)]

    while hq:
      d, u = heapq.heappop(hq)
      if d > dist[u]:
        continue
      for v, w in self.vertex[u]:
        nd = d + w
        if nd < dist[v]:
          dist[v] = nd
          heapq.heappush(hq, (nd, v))

    return dist

import sys
input = sys.stdin.readline

n, v = map(int, input().split())
start = int(input()) - 1
vertex = [[] for _ in range(n)]
for _ in range(v):
  n1, n2, v = map(lambda x: int(x) - 1, input().split())
  vertex[n1].append((n2, v+1))

dijkstra = Dijkstra(n, vertex)
result = dijkstra.dijkstra(start)

for val in result:
  if val == float("inf"):
    print("INF")
  else:
    print(val)