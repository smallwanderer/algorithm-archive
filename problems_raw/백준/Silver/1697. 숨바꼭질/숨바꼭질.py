import collections
import time

subin, imoto = map(int, input().split())
visited = [0 for _ in range(100001)]

def _isValid(loc):
  if 0 <= loc <= 100000:
    if visited[loc] == 0:
      return True
  return False

def bfs(subin, imoto):
  queue = collections.deque([subin])

  while queue:
    current = queue.popleft()
    if current == imoto:
      print(visited[current])
      return

    if _isValid(current-1):
      visited[current-1] = visited[current] + 1
      queue.append(current-1)

    if _isValid(current+1):
      visited[current+1] = visited[current] + 1
      queue.append(current+1)

    if _isValid(current*2):
      visited[current*2] = visited[current] + 1
      queue.append(current*2)


bfs(subin, imoto)

