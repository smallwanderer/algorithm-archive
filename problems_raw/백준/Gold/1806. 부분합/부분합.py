n, key = map(int, input().split())
arr = list(map(int, input().split()))
def two_pointer_1806():
  p1, p2 = 0, 0
  min_length, current_sum = float('inf'), arr[p1]

  while True:
    if current_sum < key:
      if p2+1 >= n:
        break
      p2 += 1
      current_sum += arr[p2]
    else:
      if p2-p1 < min_length:
        min_length = p2-p1
      current_sum -= arr[p1]
      p1 += 1
  return min_length+1 if min_length != float('inf') else 0

print(two_pointer_1806())
