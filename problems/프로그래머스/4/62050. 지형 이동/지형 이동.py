direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def valid_c(y, x, length):
  return 0 <= y < length and 0 <= x < length

def solution(land, height):
  import heapq

  answer = 0
  length = len(land)
  dp = [[False for _ in range(length)] for _ in range(length)]
  heap = [(0, (0, 0))]

  while heap:
    weight, coordinate = heapq.heappop(heap)
    y, x = coordinate
    if dp[y][x]:
      continue
    dp[y][x] = True
    if weight > height:
      answer += weight

    for dy, dx in direction:
      ny, nx = y + dy, x + dx
      if valid_c(ny, nx, length):
        if dp[ny][nx]:
          continue
        next_weight = abs(land[y][x] - land[ny][nx])
        heapq.heappush(heap, (next_weight, (ny, nx)))
  return answer