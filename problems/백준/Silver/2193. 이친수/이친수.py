# 이진수가 아니라 진짜 이친수다;

import sys
n = int(sys.stdin.readline().strip())

def solution(n):
  dp = [0, 1]

  for i in range(n-1):
    dp = [dp[0] + dp[1], dp[0]]

  return dp[0]+dp[1]

print(solution(n))