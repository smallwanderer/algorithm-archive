import sys

n, op = sys.stdin.readline().strip().split()
count = set()
for i in range(int(n)):
  name = sys.stdin.readline().strip()
  count.add(name)

if op == 'Y':
  print(len(count))
elif op == 'F':
  print(len(count) // 2)
elif op == 'O':
  print(len(count) // 3)