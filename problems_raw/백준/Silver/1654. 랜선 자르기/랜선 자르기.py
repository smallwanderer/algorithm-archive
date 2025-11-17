k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]
arr.sort()

def sol(n, arr):
  left, right = 1, arr[-1]
  while left <= right:
    standard = (left + right) // 2
    cnt = sum(lan // standard for lan in arr)
    if cnt >= n:
      left = standard + 1
    else:
      right = standard - 1
  return right
print(sol(n, arr))