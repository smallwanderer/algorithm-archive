
class Bellman:
  def __init__(self, v, e, graph, s=0):
    self.vertex = v
    self.edge = e
    self.graph = graph
    self.source = s
    self.INF = 10**15
    self.negative_cycle = False

  def bellman(self, source=None):
    s = self.source if source is None else source
    v = self.vertex
    g = self.graph
    INF = self.INF

    dist = [INF] * v
    predecessor = [-1] * v
    dist[s] = 0

    for i in range(v):
      updated = False
      for u, w, cost in g:
        if dist[u] != INF and dist[u]+cost < dist[w]:
          if i == v-1:
            self.negative_cycle = True
            break
          dist[w] = dist[u]+cost
          predecessor[w] = u
          updated = True
      if not updated:
        break

    self.source = s
    self.dist = dist
    self.predecessor = predecessor

  def output(self):
    """
    Modify freely depending on the types and structure of problem's output
    """
    s = self.source
    INF = self.INF

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

  bf = Bellman(v, e, edges, 0)
  bf.bellman()
  bf.output()