class Bellman:
  def __init__(self, v, e, graph):
    self.vertex = v
    self.edge = e
    self.graph = graph
    self.negative_cycle = False

  def bellman(self, source=0):
    graph = self.graph
    INF = 1e9

    dist = [INF] * self.vertex
    predecessor = [-1] * self.vertex
    dist[source] = 0

    for i in range(self.vertex-1):
      updated = False
      for u, v, cost in graph:
        if dist[u] != INF and dist[u]+cost < dist[v]:
          dist[v] = dist[u]+cost
          predecessor[v] = u
          updated = True
      if not updated:
        break

    for u, v, cost in graph:
      if dist[u] != INF and dist[u] + cost < dist[v]:
        self.negative_cycle = True

    self.source = source
    self.dist = dist
    self.predecessor = predecessor

  def output(self):
    """
    Modify freely depending on the types and structure of problem's output
    """
    s = self.source
    INF = 1e9

    if self.negative_cycle:
      print(-1)
      return

    for node, distance in enumerate(self.dist):
      if node == s:
        continue
      print(distance if distance != INF else -1)



if __name__ == "__main__":
  import sys
  input = sys.stdin.readline

  v, e = map(int, input().split())
  edges = []
  for _ in range(e):
    n1, n2, val = map(int, input().split())
    n1 -= 1
    n2 -= 1
    edges.append((n1, n2, val))

  bf = Bellman(v, e, edges)
  bf.bellman()
  bf.output()


