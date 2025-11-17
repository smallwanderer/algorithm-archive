import sys
from collections import deque


def solution():
  computers = int(sys.stdin.readline().strip())
  networks = int(sys.stdin.readline().strip())

  network = [[] for _ in range(computers + 1)]

  for _ in range(networks):
    n1, n2 = map(int, sys.stdin.readline().strip().split())
    network[n1].append(n2)
    network[n2].append(n1)

  def bfs(start):
    visited = set()
    queue = deque([start])

    while queue:
      current = queue.popleft()
      if current not in visited:
        visited.add(current)
        queue.extend(network[current])

    return len(visited) - 1

  print(bfs(1))


solution()
