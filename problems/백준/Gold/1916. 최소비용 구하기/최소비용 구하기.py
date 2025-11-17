# 최소비용 구하기 백준 1916
# https://www.acmicpc.net/problem/1916

import sys
import heapq as hq
input = sys.stdin.readline

class Dijkstra_1916:
  def __init__(self):
    self.vertex = int(input())
    self.edge = [[] for _ in range(self.vertex)]
    e = int(input())
    # a -> (w) -> b
    for _ in range(e):
      a, b, w = map(lambda x : int(x)-1, input().split())
      self.edge[a].append((w+1, b))

  def query(self, st, ed):
    edge = self.edge
    heap = [(0, st)]
    dest = [1e9] * self.vertex
    while heap:
      cv, cn = hq.heappop(heap)
      # if current node has been updated
      if dest[cn] < cv:
        continue
      # if we meet destination node return current value
      if cn == ed:
        print(cv)
        return

      for w, nn in edge[cn]:
        nv = cv + w   # new value = current value + weight
        if nv < dest[nn]:
          dest[nn] = nv # dest[next node] = new value
          hq.heappush(heap, (nv, nn))

dj_1916 = Dijkstra_1916()
start_node, end_node = map(int, input().split())
dj_1916.query(start_node-1, end_node-1)