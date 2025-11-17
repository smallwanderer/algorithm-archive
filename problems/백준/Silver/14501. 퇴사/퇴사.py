n = int(input())
a = [0] * (n + 1)
p = [0] * (n + 1)
dp = [0] * (n + 2)

for i in range(1, n + 1):
    t, pay = map(int, input().split())
    a[i] = t
    p[i] = pay

for i in range(1, n + 1):
    if i + a[i] <= n + 1:
        dp[i + a[i]] = max(dp[i + a[i]], dp[i] + p[i])

    dp[i + 1] = max(dp[i + 1], dp[i])

print(max(dp))