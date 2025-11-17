# 1865

class Bellman_1865:
  def __init__(self):
    N, M, W = map(int, input().split())
    graph = []
    for _ in range(M):
      u, v, c = map(int, input().split())
      graph.append((u, v, c))
      graph.append((v, u, c))
    for _ in range(W):
      u, v, c = map(int, input().split())
      graph.append((u, v, -c))

    # Super Source
    for i in range(N):
      graph.append((0, i+1, 0))

    self.vertex = N
    self.edge = len(graph)
    self.graph = graph
    self.cycle_detection = False

  def bellman(self, source=0):
    v = self.vertex
    e = self.edge
    g = self.graph

    INF = 1e9
    dist = [INF] * (v+1)
    dist[source] = 0

    for i in range(v+1):
      updated = False
      for j in range(e):
        u, w, cost = g[j]
        if dist[u] != INF and dist[u] + cost < dist[w]:
          if i == v:
            self.cycle_detection = True
            return
          dist[w] = dist[u] + cost
          updated = True
      if not updated:
        return

  def output(self):
    if self.cycle_detection:
      print("YES")
    else:
      print("NO")

if __name__ == "__main__":
  import sys
  input = sys.stdin.readline

  testcase = int(input())
  for _ in range(testcase):
    bell = Bellman_1865()
    bell.bellman()
    bell.output()