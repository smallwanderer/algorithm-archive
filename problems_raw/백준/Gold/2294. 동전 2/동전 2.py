import sys
def sol():
  n, k = map(int, sys.stdin.readline().split())
  dp = [int(10e4)] * (k+1)
  dp[0] = -1

  for _ in range(n):
    coin = int(sys.stdin.readline())
    if coin > k:
      continue
    dp[coin] = 1
    for i in range(coin+1, k+1):
      dp[i] = min(dp[i], dp[i-coin]+1)

  result = dp[k]
  return -1 if result == int(10e4) else result

print(sol())