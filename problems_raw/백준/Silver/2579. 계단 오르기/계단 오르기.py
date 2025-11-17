def sol():
  n = int(input())
  stairs = []
  dp = [{1: 0, 2: 0} for _ in range(n)]

  for i in range(n):
    stairs.append(int(input()))
  for i in range(n):
    stair_val = stairs[i]
    if i == 0:
      dp[i][1] = stair_val
      continue
    if i == 1:
      dp[i][1] = stair_val
      dp[i][2] = dp[i-1][1] + stair_val
      continue

    dp[i][1] = stair_val + max(val for val in dp[i-2].values())
    dp[i][2] = stair_val + dp[i-1][1]
  print(max(val for val in dp[-1].values()))
sol()