n = int(input())
channels = [input() for _ in range(n)]

current = 0
operations = []
def findChage(pos, channel):
  global current
  global operations
  idx = channels.index(channel)
  for _ in range(idx):
    operations.append('1')
    current += 1
  while channels[pos] != channel:
    channels[current], channels[current-1] = channels[current-1], channels[current]
    current -= 1
    operations.append('4')
findChage(0, "KBS1")
findChage(1, "KBS2")

print("".join(operations))

