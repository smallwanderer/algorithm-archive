import math

n = int(input())
number = list(map(int, input().split()))

result = -math.inf
dp = 0
for num in number:
  dp = dp + num
  result = max(result, dp)

  if dp < 0:
    dp = 0
print(result)
