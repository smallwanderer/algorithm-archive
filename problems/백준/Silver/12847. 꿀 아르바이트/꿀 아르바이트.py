def sliding_window_12847(arr, key):
  current_sum = sum(arr[:key])
  current_max = current_sum

  for p1 in range(len(arr) - key):
    current_sum += arr[p1+key] - arr[p1]
    current_max = max(current_max, current_sum)

  return current_max

n, key = map(int, input().split())
arr = list(map(int, input().split()))
print(sliding_window_12847(arr, key))