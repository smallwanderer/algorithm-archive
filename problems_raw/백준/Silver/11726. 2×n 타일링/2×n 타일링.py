def sol():
  n = int(input())
  dp = [1, 2]

  if n <= 2:
    print(dp[n-1])
    return

  for i in range(n-2):
    dp[1] = dp[0]+dp[1]
    dp[0] = dp[1]-dp[0]

  print(dp[-1] % 10007)

sol()
