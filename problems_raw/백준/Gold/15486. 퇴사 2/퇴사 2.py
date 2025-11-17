import sys

n = int(sys.stdin.readline().strip())
dp = [0 for i in range(n+1)]

for i in range(n):
  dur, val = map(int, sys.stdin.readline().strip().split())

  if i+dur <= n:
    dp[i+dur] = max(dp[i+dur], val+dp[i])
  dp[i+1] = max(dp[i+1], dp[i])

print(dp[-1])
