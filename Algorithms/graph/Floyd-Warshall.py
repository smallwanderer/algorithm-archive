class Floyd:
  def __init__(self, node, graph):
    self.node = node
    self.floyd_graph = graph
    self.route_graph = [[[] for _ in range(node)] for _ in range(node)]
    for i in range(self.node):
      self.floyd_graph[i][i] = 0
    self.build()

  def build(self):
    # 속성 조회 비용 최적화
    rng = range(self.node)
    graph = self.floyd_graph
    route = self.route_graph

    # k를 거쳐갈 때 최소가 되는 경로 탐색(i -> k -> j)
    for k in rng:
      for i in rng:
        for j in rng:
          if graph[i][j] > graph[i][k] + graph[k][j]:
            graph[i][j] = graph[i][k] + graph[k][j]
            route[i][j] = route[i][k] + [k] + route[k][j]


  def print_graph(self):
    for row in self.floyd_graph:
      line = []
      for v in row:
        s = "0" if v == math.inf else str(v)
        line.append(s)
      print(" ".join(line))




import math
if __name__ == "__main__":
  n, w = 5, 14
  graph = [[math.inf for _ in range(n)] for _ in range(n)]
  for _ in range(w):
    a, b, weight = map(int, input().split())
    a -= 1
    b -= 1
    graph[a][b] = min(graph[a][b], weight)
  for i in graph:
    print(i)
  print("==================")
  floyd = Floyd(n, graph)
  floyd.print_graph()

"""
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
"""