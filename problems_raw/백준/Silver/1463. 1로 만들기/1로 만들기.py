import math
import sys
sys.setrecursionlimit(10**6)
def solution():
  X = int(input())
  dp = [-1 for _ in range(X+1)]
  dp[1] = 0

  def make_1(x):
    if x == 1:
      return 0

    count_1, count_2, count_3 = math.inf, math.inf, math.inf

    if x % 3 == 0:
      if dp[x//3] != -1:
        count_3 = dp[x//3]
      else:
        count_3 = make_1(x//3)

    if x % 2 == 0:
      if dp[x//2] != -1:
        count_2 = dp[x//2]
      else:
        count_2 = make_1(x//2)

    if dp[x-1] != -1:
      count_1 = dp[x-1]
    else:
      count_1 = make_1(x-1)

    count = 1 + min(count_1, count_2, count_3)
    if dp[x] != -1:
      dp[x] = min(count, dp[x])
    else:
      dp[x] = count

    #print(f"current x is {x} and dp is {dp}")
    return count

  make_1(X)
  print(dp[X])

solution()
