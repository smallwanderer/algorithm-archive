# 1219

class Bellman_1219:
  def __init__(self):
    N, st, ed, M = map(int, input().split())
    graph = []
    for _ in range(M):
      u, v, c = map(int, input().split())
      graph.append((u, v, -c))
    pay = list(map(int, input().split()))

    self.vertex = N
    self.edge = M
    self.graph = graph
    self.pay = pay

    print(self.bellman(st, ed))

  def bellman(self, s, e):
    INF = -1e9
    g = self.graph
    v = self.vertex
    pay = self.pay
    dist = [INF] * v
    cycle_node = [False] * v
    dist[s] = pay[s]

    for i in range(v):
      updated = False
      for u, f, c in g:
        if dist[u] != INF and dist[u] + c + pay[f] > dist[f]:

          # cycle-detected => BFS to check
          if i == v-1:
            import collections
            stack = collections.deque([u])

            while stack:
              cycle_cur = stack.popleft()
              if cycle_cur == e:
                return 'Gee'
              if cycle_node[cycle_cur]:
                continue
              cycle_node[cycle_cur] = True
              for cycle_u, cycle_f, cycle_c in g:
                if cycle_u == cycle_cur and not cycle_node[cycle_f]:
                  stack.append(cycle_f)

          dist[f] = dist[u] + c + pay[f]
          updated = True
      if not updated:
        break

    if dist[e] != INF:
        return dist[e]
    else:
      return 'gg'


import sys
input = sys.stdin.readline

bell = Bellman_1219()