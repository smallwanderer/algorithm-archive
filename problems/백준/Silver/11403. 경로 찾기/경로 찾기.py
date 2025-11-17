class Floyd:
  def __init__(self, node, graph):
    self.node = node
    self.floyd_graph = graph
    # self.route_graph = [[[] for _ in range(node)] for _ in range(node)]
    # for i in range(self.node):
    #   self.floyd_graph[i][i] = 0
    self.build(self.floyd_graph)

  def build(self, graph):
    floyd_graph = graph
    for k in range(self.node):
      for i in range(self.node):
        for j in range(self.node):
          we = floyd_graph[i][j] or (floyd_graph[i][k] and floyd_graph[k][j])
          # if we != floyd_graph[i][j]:
          #   self.route_graph[i][j].append(k)
          floyd_graph[i][j] = we
    self.floyd_graph = floyd_graph

import sys
input = sys.stdin.readline

n = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
  arr = list(map(int, input().split()))
  for j, val in enumerate(arr):
    if val == 1:
      graph[i][j] = 1

floyd = Floyd(n, graph)

for row in floyd.floyd_graph:
  line = []
  for v in row:
    s = "1" if v != 0 else "0"
    line.append(s)
  print(" ".join(line))