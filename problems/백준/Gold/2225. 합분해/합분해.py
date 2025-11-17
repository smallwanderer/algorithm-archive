import sys

def solution():
  n, k = map(int, sys.stdin.readline().split())
  dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
  dp[0] = [1] * (k+1)

  for i in range(1, n+1):
    for j in range(1, k+1):
      if j == 1:
        dp[i][j] = 1
      else:
        dp[i][j] = sum(dp[k][j-1] for k in range(i+1))

  return dp[n][k]


print(solution() % 1000000000)