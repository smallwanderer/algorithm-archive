from collections import deque
n, m, v = map(int, input().split())

def solution(n, m, v):
  nodes = [[] for _ in range(n+1)]
  # 방향이 없는 그래프
  for i in range(m):
    n1, n2 = map(int, input().split())
    nodes[n1].append(n2)
    nodes[n2].append(n1)

  dfs(nodes, v)
  print()
  bfs(nodes, v)

def dfs(nodes, v):
  dp = [False for _ in range(len(nodes))]
  nodes = [sorted(n, reverse=True) for n in nodes]
  stack = deque([v])
  while stack:
    node = stack.pop()
    if dp[node]:
      continue
    dp[node] = True
    for ad_nodes in nodes[node]:
      if not dp[ad_nodes]:
        stack.append(ad_nodes)
    print(node, end=" ")

def bfs(nodes, n):
  dp = [False for _ in range(len(nodes))]
  nodes = [sorted(n) for n in nodes]
  queue = deque([v])
  while queue:
    node = queue.pop()
    if dp[node]:
      continue
    dp[node] = True
    for ad_nodes in nodes[node]:
      if not dp[ad_nodes]:
        queue.appendleft(ad_nodes)
    print(node, end=" ")

solution(n, m, v)
