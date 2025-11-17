import sys

n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
dp = [0]

for i in range(n):
  dp.append(dp[i] + numbers[i])

for _ in range(m):
  a, b = map(int, sys.stdin.readline().split())
  print(dp[b]-dp[a-1])
