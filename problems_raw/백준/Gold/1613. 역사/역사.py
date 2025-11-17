class Floyd:
  def __init__(self, node, graph):
    self.node = node
    self.floyd_graph = graph
    self.build()

  def build(self):
    n = self.node
    g = self.floyd_graph
    rng = range(n)
    for k in rng:
      nodes_k = g[k]
      for i in rng:
        nodes_i = g[i]
        i_to_k = nodes_i[k]
        for j in rng:
          if i_to_k == nodes_k[j]:
            nodes_i[j] = nodes_i[j] or i_to_k

  def search(self, a, b):
    return self.floyd_graph[a][b]

import sys
input = sys.stdin.readline

n, g = map(int, input().split())
graph = [[0 for _ in range(n)] for _ in range(n)]
for i in range(g):
  a, b = map(lambda x: int(x)-1, input().split())
  graph[a][b] = -1
  graph[b][a] = 1

floyd = Floyd(n, graph)

q = int(input())
for _ in range(q):
  a, b = map(lambda x: int(x)-1, input().split())
  print(floyd.search(a, b))
