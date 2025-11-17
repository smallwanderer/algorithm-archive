def solution():
  n = int(input())
  if n % 2 == 1:
    return 0
  n = n // 2

  dp = [0] * (n + 1)
  dp[0], dp[1] = 1, 3

  for i in range(2, n+1):
    dp[i] = dp[i-1] * 3
    for j in range(i-1):
      dp[i] += dp[j]*2

  return dp[-1]

print(solution())
