# 백준 1766 : 위상 정렬
# - Kahn & Priority Queue

import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
edges = [[] for _ in range(v+1)]
incoming = [0 for _ in range(v+1)]
for _ in range(e):
  a, b = map(int, input().split())
  edges[a].append(b)
  incoming[b] += 1

def kahn_problemSheet():
  queue = [x for x in range(1, v+1) if incoming[x] == 0]
  result = []
  while queue:
    current = heapq.heappop(queue)
    result.append(current)
    for next in edges[current]:
      incoming[next] -= 1
      if incoming[next] == 0:
        heapq.heappush(queue, next)
  return result

for vertex in kahn_problemSheet():
  print(vertex, end=" ")