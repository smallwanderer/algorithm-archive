import heapq
import time

arr =[123, 12, 32, 3]
heapq.heapify(arr)
print(heapq.heappop(arr))

class Dijkstra:
  """
  Dijkstra Algorithm

  음이 아닌 가중치를 갖는 유향 그래프에서의 단일 소스 최단 경로 알고리즘
  """
  def __init__(self, n, v):
    import time
    """
    Parameters
    ----------
    n (int) : 탐색하는 노드의 수 (o-indexed)
    v ([int][(int, int)]) : i번째 노드와 연결된 모든 j의 인접 리스트
    """
    self.node = n
    self.vertex = v

    rng = range(n)
    self.dist = [1e9 for _ in rng]
    self.visited = [False for _ in rng]
    self.previous = [None for _ in rng]


  def dijkstra(self, st):
    dist = self.dist
    previous = self.previous
    dist[st] = 0
    hq = [(0, st)]

    while hq:
      cd, cn = heapq.heappop(hq)
      if cd > dist[cn]: # if the node has been updated
        continue
      for nn, w in self.vertex[cn]: # update from current node
        nd = cd + w
        if nd < dist[nn]: # greedy
          dist[nn] = nd
          previous[nn] = cn
          heapq.heappush(hq, (nd, nn))

    return dist, previous


if __name__ == "__main__":
  import sys
  input = sys.stdin.readline

  n, v = map(int, input().split())
  start = int(input()) - 1
  vertex = [[] for _ in range(n)]
  for _ in range(v):
    n1, n2, v = map(lambda x: int(x) - 1, input().split())
    vertex[n1].append((n2, v+1))

  dijkstra = Dijkstra(n, vertex)
  result = dijkstra.dijkstra(0)

  print(result[0])
  print(result[1])