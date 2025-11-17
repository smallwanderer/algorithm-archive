import sys

def solution():
  n = int(sys.stdin.readline().strip())
  dp = [0, 0, 0]

  for _ in range(n):
    R, G, B = map(int, sys.stdin.readline().split())
    temp = [0, 0, 0]
    temp[0] = min(dp[1], dp[2]) + R
    temp[1] = min(dp[0], dp[2]) + G
    temp[2] = min(dp[0], dp[1]) + B
    dp = [temp[0], temp[1], temp[2]]

  return min(dp)

print(solution())
