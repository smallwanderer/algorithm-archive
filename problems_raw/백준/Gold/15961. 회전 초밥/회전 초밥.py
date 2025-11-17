import collections
import sys
def sliding_window_15961(n, arr, k, c):
  # 배열에서 선택한 연속된 k개의 요소의 종류의 수 최대 출력
  sub_arr = collections.defaultdict(int)
  current_sum = 0
  for i in range(k):
    if sub_arr[arr[i]] == 0:
      current_sum += 1
    sub_arr[arr[i]] += 1

  if sub_arr[c] == 0:
    current_sum += 1
  sub_arr[c] += 1

  max_sum = current_sum

  for i in range(n):
    p1 = arr[i]
    p2 = arr[(i + k) % n]

    sub_arr[p1] -= 1
    if sub_arr[p1] == 0:
      current_sum -= 1

    if sub_arr[p2] == 0:
      current_sum += 1
    sub_arr[p2] += 1

    max_sum = max(max_sum, current_sum)

  return max_sum

data = sys.stdin.read().split()
print(sliding_window_15961(int(data[0]),
                           list(map(int, data[4:])),
                           int(data[2]),
                           int(data[3])))
