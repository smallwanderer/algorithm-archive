class Floyd:
  def __init__(self, node, graph):
    self.node = node
    self.floyd_graph = graph
    for i in range(self.node):
      self.floyd_graph[i][i] = 0
    self.build()

  def build(self):
    for k in range(self.node):
      for i in range(self.node):
        for j in range(self.node):
          we = min(self.floyd_graph[i][j], self.floyd_graph[i][k] + self.floyd_graph[k][j])
          self.floyd_graph[i][j] = we

  def print_graph(self):
    for row in self.floyd_graph:
      line = []
      for v in row:
        s = "0" if v == math.inf else str(v)
        line.append(s)
      print(" ".join(line))


import math
n = int(input())
w = int(input())

graph = [[math.inf for _ in range(n)] for _ in range(n)]
for _ in range(w):
    a, b, weight = map(int, input().split())
    a -= 1
    b -= 1
    graph[a][b] = min(graph[a][b], weight)
floyd = Floyd(n, graph)
floyd.print_graph()