n = int(input())
fluids = sorted(list(map(int, input().split())))

def two_pointers_2470():
  p1, p2 = 0, n-1
  current_min = (float('inf'), float('inf'))

  while p1 < p2:
    p1_val, p2_val = fluids[p1], fluids[p2]
    if abs(p1_val+p2_val) < abs(sum(current_min)):
      current_min = (p1_val, p2_val)
    if abs(p1_val) > abs(p2_val):
      p1 += 1
    else:
      p2 -= 1

  return current_min

print(*two_pointers_2470())
