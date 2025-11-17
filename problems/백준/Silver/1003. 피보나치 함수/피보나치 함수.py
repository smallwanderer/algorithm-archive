n = int(input())
dp = [(1, 0), (0, 1)]

for _ in range(n):
  test = int(input())

  if test < len(dp):
    print(*dp[test])
    continue

  for i in range(len(dp), test+1):
    dp.append((dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]))
  print(*dp[test])


