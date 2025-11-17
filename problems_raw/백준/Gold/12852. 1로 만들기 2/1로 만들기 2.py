x = int(input())

def bfs(x):
  from collections import deque
  queue = deque([x])
  dp = {x: [x]}

  while queue:
    x = queue.popleft()

    if x == 1:
      return dp[1]

    if x % 3 == 0 and x//3 not in dp:
      dp[x//3] = dp[x] + [x//3]
      queue.append(x//3)
    if x % 2 == 0 and x//2 not in dp:
      dp[x//2] = dp[x] + [x//2]
      queue.append(x//2)
    if x-1 not in dp:
      dp[x-1] = dp[x] + [x-1]
      queue.append(x-1)


result = bfs(x)
print(len(result)-1)
print(*result)