import sys

input = sys.stdin.readline

n = int(input())
pan = [input() for _ in range(n)]

def where_heart(arr):
  for i in range(n):
    for j in range(n):
      if arr[i][j] == '*':
        return (i+1, j)

def isValid(y, x):
  return 0 <= x < n and 0 <= y < n

def sol(arr):
  heart_pos = where_heart(arr)
  print(heart_pos[0]+1, heart_pos[1]+1)
  direction = [(0, -1), (0, 1), (1, 0)]
  result = []

  for dy, dx in direction:
    y, x = heart_pos[0], heart_pos[1]
    cnt = 0
    while isValid(y + dy, x + dx):
      if arr[y + dy][x + dx] == '*':
        cnt += 1
        y, x = y + dy, x + dx
      else:
        break
    result.append(cnt)
    if dx == 0:
      for t in range(2):
        if t == 0:
          ty, tx = y + 1, x - 1
        else:
          ty, tx = y + 1, x + 1
        cnt = 0
        while isValid(ty, tx):
          if arr[ty][tx] == '*':
            cnt += 1
            ty, tx = ty + 1, tx
          else:
            break
        result.append(cnt)

  print(*result, sep=' ')

sol(pan)