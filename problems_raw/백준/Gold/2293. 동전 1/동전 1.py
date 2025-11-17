def sol():
  n, k = map(int, (input().split()))
  coins = []
  dp = [0] * (k+1)
  dp[0] = 1
  for _ in range(n):
    coins.append(int(input()))
  coins.sort()

  for i in range(len(coins)):
    for j in range(coins[i], k+1):
      dp[j] = dp[j] + dp[j-coins[i]]
  print(dp[k])
  
  
sol()