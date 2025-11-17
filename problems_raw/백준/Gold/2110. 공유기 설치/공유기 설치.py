n, c = map(int, input().split())
x = list(sorted([int(input()) for _ in range(n)]))

"""
목표 : key보다 큰 값 중 가장 작은 값의 인덱스를 반환해야 함. 
없는 경우, None을 반환.

start (index) : 현재로부터 key 이후의 값을 찾아야 함
key : start보다 key만큼 큰 값 중 가장 작은 값의 인덱스 반환
x : 찾아야 하는 sorted list
"""
def interpolation_search(start, key_offset, x):
  left, right = start, len(x) - 1
  target = x[left] + key_offset
  while left <= right:
    mid = (left + right) // 2
    if x[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  if left < len(x):
    return left
  return None

def solution(n, c, x):
  left, right = 1, x[-1] - x[0]
  result = 0

  while left <= right:
    mid = (left + right) // 2

    next = 0
    for _ in range(c-1):
      next = interpolation_search(next, mid, x)
      if next is None:
        break

    if next is None:
      right = mid - 1
    else:
      result = mid
      left = mid + 1

  return result

print(solution(n, c, x))