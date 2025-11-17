import sys

n, k = map(int, sys.stdin.readline().strip().split())
country = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
country.sort(key=lambda x: (-x[1], -x[2], -x[3]))

def sol():
  rank = 1
  for c_idx in range(n-1):
    if country[c_idx][0] == k:
      return str(rank)
    if country[c_idx][1:] != country[c_idx+1][1:]:
      rank = c_idx+2
  return str(rank)

sys.stdout.write(sol())

