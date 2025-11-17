def sol():
  n = int(input())
  dp = [0, 1, 2, 4]
  flag = 3

  for i in range(n):
    x = int(input())
    if flag >= x:
      print(dp[x])
      continue

    for i in range(flag, x):
      dp.append(dp[i] + dp[i-1] + dp[i-2])
    flag = x

    print(dp[-1])
sol()