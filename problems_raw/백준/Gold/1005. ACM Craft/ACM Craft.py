# 백준 1005 : 위상정렬
# - kahn

import sys
import collections
input = sys.stdin.readline

def kahn_ACM(nodes, edges, re_edges, incoming, target):
  dp = [0]
  dp.extend(nodes)
  queue = [x for x in range(1, len(nodes)+1) if incoming[x] == 0]
  queue = collections.deque(queue)
  while queue:
    current = queue.popleft()
    for next in edges[current]:
      incoming[next] -= 1
      if incoming[next] == 0:
        queue.append(next)
        dp[next] += max(dp[x] for x in re_edges[next])
  return dp[target]


t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  node_weight = list(map(int, input().split()))
  edges = [[] for _ in range(n+1)]
  reverse_edge = [[] for _ in range(n+1)]
  incoming = [0 for _ in range(n+1)]
  for _ in range(m):
    node1, node2 = map(int, input().split())
    edges[node1].append(node2)
    reverse_edge[node2].append(node1)
    incoming[node2] += 1
  target = int(input())
  print(kahn_ACM(node_weight, edges, reverse_edge, incoming, target))