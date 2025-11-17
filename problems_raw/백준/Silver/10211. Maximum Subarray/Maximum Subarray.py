import sys
input = sys.stdin.readline

def kadane(n, array):
  dp = 0
  maximum_sum = -sys.maxsize
  for num in array:
    dp = max(dp+num, num)
    maximum_sum = max(dp, maximum_sum)
  return maximum_sum

t = int(input())
for _ in range(t):
  n = int(input())
  array = list(map(int, input().split()))
  print(kadane(n, array))