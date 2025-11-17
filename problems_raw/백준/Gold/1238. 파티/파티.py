import sys
import heapq as hq
input = sys.stdin.readline

class Dijkstra_1238:
  # 1-indexed
  def __init__(self):
    self.vertex, e, self.ed = map(int, input().split())
    self.edge = [[] for _ in range(self.vertex+1)]

    # a -> (w) -> b
    for _ in range(e):
      a, b, w = map(int, input().split())
      self.edge[a].append((w, b))

  def dijkstra(self, st, ed):
    e = self.edge
    dist = [1e9] * (self.vertex + 1)
    dist[st] = 0
    heap = [(0, st)]
    while heap:
      cv, cn = hq.heappop(heap)
      if dist[cn] < cv:
        continue
      if ed and cn == ed:
        return cv

      for w, nn in e[cn]:
        nv = cv + w
        if dist[nn] > nv:
          dist[nn] = nv
          hq.heappush(heap, (nv, nn))
    return dist

  def rev_query(self):
    return self.dijkstra(self.ed, None)

  def query(self):
    v = self.vertex
    end = self.ed
    e = self.edge

    rev_query = self.rev_query()
    maximum = -1
    for i in range(1, v+1):
      if i == end:
        continue
      maximum = max(maximum, self.dijkstra(i, end) + rev_query[i])

    print(maximum)
    return

dj = Dijkstra_1238()
dj.query()