import sys
import time

def solution():
  col, row = map(int, sys.stdin.readline().split())
  map_input = [list(map(int, sys.stdin.readline().split())) for _ in range(col)]
  dp = [[{'up': 0, 'down': 0, 'left': 0, 'right': 0} for _ in range(row)] for _ in range(col)]
  flag = [['F' for _ in range(row)] for _ in range(col)]
  dp[0][0]['up'] = 1 # entrance
  queue = [(0, 0)] # BFS

  def isValid(y, x) -> bool:
    if 0<=y<col and 0<=x<row:
      return True
    return False

  direction = {'down': (1,0), 'up': (-1, 0), 'right': (0, 1), 'left': (0, -1)}
  queue_cnt = 0
  while queue:
    y, x = queue.pop(0)
    flag[y][x] = 'T'
    for dir_dp, d in direction.items():
      ny, nx = y + d[0], x + d[1]
      if isValid(ny, nx):
        current_sum = sum(dp[y][x].values())
        if map_input[ny][nx] < map_input[y][x]:
          dp[ny][nx][dir_dp] = current_sum
          if (ny, nx) not in queue:
            queue.append((ny, nx))
            flag[ny][nx] = 'F'
    # queue_cnt += 1
    # if queue_cnt % 1 == 0:
    #   print(f"current ({y}, {x}), queue: {queue} => ")
    #   for i in range(col):
    #     print(list(sum(item.values()) for item in dp[i]), '\t', flag[i])
    #   print()
    #   time.sleep(0)
  print(sum(dp[col-1][row-1].values()))

solution()
