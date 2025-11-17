n = int(input())
cnt, inc, result = 0, 1, 0
while True:
  if n <= result+1:
    print(inc)
    break
  cnt += inc
  result = cnt * 6
  inc += 1
