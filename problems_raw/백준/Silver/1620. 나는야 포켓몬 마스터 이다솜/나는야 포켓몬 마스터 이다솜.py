# HASH TABLE
import sys

n, m = map(int, sys.stdin.readline().split())
pocket_id = dict()
pocket_name = dict()
for i in range(1, n+1):
  name = sys.stdin.readline().strip()
  # if (65 <= ord(name[-1]) <= 90):
  #   name = chr(ord(name[0]) - 32) + name[1:-1] + chr(ord(name[-1]) + 32)

  pocket_id[i] = name
  pocket_name[name] = i

for k in range(m):
  question = sys.stdin.readline().strip()

  if all(48 <= ord(q) <= 57 for q in question):
    print(pocket_id[int(question)])
  else:
    print(pocket_name[question])