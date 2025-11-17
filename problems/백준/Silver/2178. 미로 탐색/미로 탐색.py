import collections

n, m = map(int, input().split())
table = [input() for _ in range(n)]

def bfs():
  global table
  direction = {(1, 0), (0, 1), (-1,0), (0,-1)}
  dp = [[0 for _ in range(m)] for _ in range(n)]
  dp[0][0] = 1
  queue = collections.deque([(0, 0)])
  while queue:
    y, x = queue.popleft()
    if y == n-1 and x == m-1:
      print(dp[y][x])
      return

    for dy, dx in direction:
      if 0 <= y+dy < n and 0 <= x+dx < m and table[y+dy][x+dx] == '1':
        if dp[y+dy][x+dx] == 0:
          dp[y+dy][x+dx] = 1 + dp[y][x]
          queue.append((y+dy, x+dx))

bfs()