
n, m = map(int, input().split())
trees = list(map(int, input().split()))

def solution(m, trees):
  left, right = 0, max(trees)

  while left <= right:
    mid = (left + right) // 2
    cut_down = sum(x-mid if x > mid else 0 for x in trees)
    if cut_down < m:
      right = mid - 1
    else:
      left = mid + 1

  return right

print(solution(m, trees))