n, score, p = map(int, input().split())
ranking = list(map(int, input().split())) if n > 0 else []
ranking.extend([-1 for _ in range(p-n)])

def sol():
  rank = -1
  for idx, val in enumerate(ranking):
    if val == score and rank == -1:
      rank = idx
    if val < score:
      return idx+1 if rank == -1 else rank+1
  return -1

print(sol())