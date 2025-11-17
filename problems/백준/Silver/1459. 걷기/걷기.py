import sys

def solution():
  result = 0
  coord_min, coord_max = min(x, y), max(x, y)
  # diag
  if s > 2*w:
    result += coord_min * (2*w)
  else:
    result += coord_min * s
  # straight
  if s < w:
    result += (coord_max - coord_min) * s
    if (coord_max-coord_min) % 2 != 0:
      result += w-s
  else:
    result += (coord_max - coord_min) * w

  print(result)
  return


x, y, w, s = map(int, sys.stdin.readline().strip().split())
solution()