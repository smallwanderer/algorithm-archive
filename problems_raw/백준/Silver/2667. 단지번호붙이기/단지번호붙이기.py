import sys

apart_complex = int(sys.stdin.readline().strip())
table = [sys.stdin.readline().strip() for _ in range(apart_complex)]
dp = [[0 for _ in range(apart_complex)] for _ in range(apart_complex)]

def solution(table):
  global dp
  result = []
  for y in range(apart_complex):
    for x in range(apart_complex):
      if dp[y][x] == 0 and table[y][x] == '1':
        result.append(dfs(y,x))

  print(len(result))
  for num in sorted(result):
    print(num)

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def dfs(y, x):
  global dp
  result = 1
  dp[y][x] = 1

  for dy, dx in directions:
    if 0 <= y+dy < apart_complex and 0 <= x+dx < apart_complex:
      if dp[y+dy][x+dx] == 0 and table[y+dy][x+dx] == '1':
        result += dfs(y+dy, x+dx)

  return result

solution(table)