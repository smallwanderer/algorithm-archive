# 백준 2252 : Topology Sort
# - Kahn

import sys
import collections

v, e = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(v+1)]
incoming = [0 for _ in range(v+1)]

for _ in range(e):
  n1, n2 = map(int, sys.stdin.readline().split())
  edges[n1].append(n2)
  incoming[n2] += 1

def kahn():
  result = []
  queue = [x for x in range(1, v + 1) if incoming[x] == 0]
  queue = collections.deque(queue)
  while queue:
    current = queue.popleft()
    result.append(current)
    for next in edges[current]:
      incoming[next] -= 1
      if incoming[next] == 0:
        queue.append(next)
  return result

for result in kahn():
  print(result, end=" ")