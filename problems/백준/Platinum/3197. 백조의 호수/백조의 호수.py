import sys, collections

inp = sys.stdin.read()
data = inp.split("\n")
height, width = map(int, data[0].split())
grid = [list(row) for row in data[1:height+1]]
dp = [[-1 for _ in range(width)] for _ in range(height)]  # (day, swan_type)
water_temp_queue = []
swan_temp_queue = []
for i in range(height):
  for j in range(width):
    if grid[i][j] == "L":
      swan_temp_queue.append((i, j))
    elif grid[i][j] == ".":
      water_temp_queue.append((i, j))
grid[swan_temp_queue[0][0]][swan_temp_queue[0][1]] = 's'
grid[swan_temp_queue[1][0]][swan_temp_queue[1][1]] = 'S'
dp[swan_temp_queue[0][0]][swan_temp_queue[0][1]] = 0
dp[swan_temp_queue[1][0]][swan_temp_queue[1][1]] = 0
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def bfs():
  day = 0
  while True:
    swan_queue = collections.deque(swan_temp_queue)
    swan_temp_queue.clear()
    while swan_queue:
      sy, sx = swan_queue.popleft()
      for dy, dx in direction:
        ny, nx = sy + dy, sx + dx
        # meets swan2 pool
        if 0 <= ny < height and 0 <= nx < width:
          if (grid[sy][sx] == 's' and grid[ny][nx] == 'S') or (grid[sy][sx] == 'S' and grid[ny][nx] == 's'):
            return max(dp[sy][sx], dp[ny][nx])

          # meets ice
          if grid[ny][nx] == "X":
            grid[ny][nx] = grid[sy][sx]
            dp[ny][nx] = day + 1
            swan_temp_queue.append((ny, nx))

          # meets another water pool
          if grid[ny][nx] == ".":
            queue_temp = collections.deque([(sy, sx)])
            while queue_temp:
              ty, tx = queue_temp.popleft()
              for t_dy, t_dx in direction:
                tny, tnx = ty + t_dy, tx + t_dx
                if 0 <= tny < height and 0 <= tnx < width:
                  if grid[tny][tnx] == ".":
                    queue_temp.append((tny, tnx))
                    grid[tny][tnx] = grid[ty][tx]
                    dp[tny][tnx] = day
                  elif grid[tny][tnx] == "X":
                    swan_temp_queue.append((tny, tnx))
                    dp[tny][tnx] = day + 1
                  elif (grid[ty][tx] == 's' and grid[tny][tnx] == 'S') or (grid[ty][tx] == 'S' and grid[tny][tnx] == 's'):
                    return max(dp[ty][tx], dp[tny][tnx])
                  grid[tny][tnx] = grid[ty][tx]

          # meets ice
          if grid[ny][nx] == "X":
            grid[ny][nx] = grid[sy][sx]
            dp[ny][nx] = day + 1
            swan_temp_queue.append((ny, nx))

    water_queue = collections.deque(water_temp_queue)
    water_temp_queue.clear()
    while water_queue:
      wy, wx = water_queue.popleft()
      if grid[wy][wx] != ".":
        continue
      for dy, dx in direction:
        ny, nx = wy + dy, wx + dx
        if 0 <= ny < height and 0 <= nx < width:
          if grid[ny][nx] == "X":
            water_temp_queue.append((ny, nx))
            dp[ny][nx] = day + 1
            grid[ny][nx] = "."

    day += 1
print(bfs())