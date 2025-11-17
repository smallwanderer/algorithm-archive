import sys
import copy

n, k = map(int, sys.stdin.readline().strip().split())
burden = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
dp = {0: 0}

for weight, value in burden:
  if weight > k:
    continue
  temp = copy.deepcopy(dp)
  for key, val in temp.items():
    if weight + key <= k:
      dp[weight + key] = max(dp.get(weight + key, 0), val + value)

  dp[weight] = max(dp.get(weight, 0), value)

print(max(dp.values() if dp else 0))