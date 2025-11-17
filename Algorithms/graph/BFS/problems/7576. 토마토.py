import sys
import collections
import numpy as np
import time

# m, n, h = map(int, sys.stdin.readline().strip().split())
m, n, h = 100, 100, 100
dp = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
# tomatoes = [[list(map(int, sys.stdin.readline().strip().split()))for _ in range(n)] for _ in range(h)]
random_value = 42
np.random.seed(random_value)
tomatoes = np.random.choice([-1, 0, 1], size=(h, n, m), p=[0.1, 0.7, 0.2])

start_time = time.perf_counter_ns()

start_tomatoes = [(z, y, x) for z, layer in enumerate(tomatoes)
                  for y, tomato_line in enumerate(layer)
                  for x, tomato in enumerate(tomato_line)
                  if tomato == 1]
direction = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

def bfs():
  queue = collections.deque(start_tomatoes)
  while queue:
    current_z, current_y, current_x = queue.popleft()
    for dz, dy, dx in direction:
      n_z, n_y, n_x = current_z+dz, current_y+dy, current_x+dx
      if is_valid(n_z, n_y, n_x):
        if dp[n_z][n_y][n_x] == 0:
          dp[n_z][n_y][n_x] = dp[current_z][current_y][current_x] + 1
          queue.append((n_z, n_y, n_x))

def is_valid(nh, nn, nm):
  if 0<=nh<h and 0<=nn<n and 0<=nm<m:
    if tomatoes[nh][nn][nm] == 0:
      return True
  return False

def solution():
  bfs()
  flatten_dp = list(dp_x for dp_z in dp for dp_y in dp_z for dp_x in dp_y)
  flatten_tomatoes = list(tomato_x for tomato_z in tomatoes for tomato_y in tomato_z for tomato_x in tomato_y)
  for x, y in zip(flatten_dp, flatten_tomatoes):
    if y == 0 and x == 0:
      print(-1)
      return
  print(max(tomato for layer in dp for tomato_line in layer for tomato in tomato_line))

solution()
end_time = time.perf_counter_ns()
print(end_time-start_time)