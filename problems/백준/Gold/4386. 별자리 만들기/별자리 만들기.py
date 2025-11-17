# 별자리 만들기 4386 : MST
# - Prim

import sys
import math
import heapq

# Number of Star
n = int(sys.stdin.readline())
coordinates = []
for _ in range(n):
  coordinates.append(tuple(map(float, sys.stdin.readline().split())))

def prim_make_zodiac(coordinates):
  def _euclidean_distance(coord1, coord2):
    x = coord2[0] - coord1[0]
    y = coord2[1] - coord1[1]
    return math.sqrt(x**2 + y**2)

  dp = set()
  queue = [(0, coordinates[0])]
  weight_sum = 0

  while queue:
    weight, current = heapq.heappop(queue)
    if current in dp:
      continue

    weight_sum += weight
    dp.add(current)

    if len(dp) == len(coordinates):
      return f"{weight_sum:.2f}"

    for idx, coord in enumerate(coordinates):
      if coord in dp:
        continue
      weight = _euclidean_distance(current, coord)
      heapq.heappush(queue, (weight, coord))

print(prim_make_zodiac(coordinates))
