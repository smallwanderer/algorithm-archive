import sys
import collections

people = int(sys.stdin.readline().strip())
n1, n2 = map(int, sys.stdin.readline().strip().split())
relation = int(sys.stdin.readline().strip())
relationship = [[] for _ in range(people+1)]
for i in range(relation):
  r1, r2 = map(int, sys.stdin.readline().strip().split())
  relationship[r1].append(r2)
  relationship[r2].append(r1)

dp = [0] * (people+1)
def bfs(n, key):
  queue = collections.deque([n])
  while queue:
    current = queue.popleft()
    if current == key:
      return dp[current]
    for ad_node in relationship[current]:
      if dp[ad_node] == 0:
        dp[ad_node] = dp[current] + 1
        queue.append(ad_node)

  return -1

print(bfs(n1, n2))


