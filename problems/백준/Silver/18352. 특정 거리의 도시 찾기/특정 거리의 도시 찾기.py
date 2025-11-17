# 백준 18352
# https://www.acmicpc.net/problem/18352

import sys
import heapq as hq
input = sys.stdin.readline

class Dijkstra_18352:
  # 1-indexed
  def __init__(self):
    self.v, e, self.k, self.st = map(int, input().split())
    self.edge = [[] for _ in range(self.v + 1)]
    for _ in range(e):
      a, b = map(int, input().split())
      self.edge[a].append(b)

  def query(self):
    v = self.v
    edge = self.edge
    dest = [v+1 for _ in range(v+1)] # max is v+1
    dest[self.st] = 0
    heap = [(0, self.st)]
    while heap:
      cv, cn = hq.heappop(heap)
      if dest[cn] < cv:
        continue

      for nn in edge[cn]:
        if dest[nn] > cv+1:
          dest[nn] = cv+1
          hq.heappush(heap, (cv+1, nn))

    k = self.k
    flag = False
    for idx, v in enumerate(dest):
      if v != k:
        continue
      print(idx)
      flag = True
      
    if not flag:
      print(-1)

dj_18352 = Dijkstra_18352()
dj_18352.query()