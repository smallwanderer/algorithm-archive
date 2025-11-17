import sys
sys.setrecursionlimit(10000)
def solution():
  n = int(sys.stdin.readline())
  board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

  direction = {(0, 1), (1, 0)} # right, down
  dp = [[-1 for _ in range(n)] for _ in range(n)]

  def dfs(coord):
    cases = 0
    y, x = coord
    current = board[y][x]
    if y == n-1 and x == n-1:
      return 1
    if current == 0:
      return 0

    for dy, dx in direction:
      dy, dx = dy * current, dx * current
      if y + dy < n and x + dx < n:
        if dp[y+dy][x+dx] != -1:
          cases += dp[y+dy][x+dx]
        else:
          cases += dfs((y + dy, x + dx))

    dp[y][x] = cases
    return cases

  return dfs((0, 0))

print(solution())
