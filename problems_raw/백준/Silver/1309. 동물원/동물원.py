import sys

def solution():
  n = int(sys.stdin.readline())
  dp = [1, 1]

  for i in range(1, n+1):
    dp[0] = dp[1]*2 + dp[0]
    dp[1] = dp[0] - dp[1]

  return dp[0] % 9901

print(solution())