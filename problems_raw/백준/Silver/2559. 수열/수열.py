n, k = map(int, input().split())
arr = list(map(int, input().split()))

def prefix_sum_2559(n, k, arr):
  current = sum(arr[:k])
  result = current

  for i in range(n-k):
    current -= arr[i]
    current += arr[i+k]
    result = max(current, result)

  print(result)

prefix_sum_2559(n, k, arr)