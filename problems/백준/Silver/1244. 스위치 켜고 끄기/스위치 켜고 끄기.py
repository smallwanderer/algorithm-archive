switch = int(input())
switches = list(map(int, input().split()))

operation = int(input())
operations = [tuple(map(int, input().split())) for _ in range(operation)]

def switch_operation(operation):
  global switches

  sex, value = operation
  idx = 1
  if sex == 1:
    while True:
      if value * idx - 1 >= len(switches):
        break
      switches[value * idx - 1] = ~switches[value * idx - 1] & 1
      idx += 1
  else:
    switches[value - 1] = ~switches[value - 1] & 1
    while True:
      if 0 > value-idx-1 or value+idx-1 >= len(switches):
        break
      left, right = switches[value-idx-1], switches[value+idx-1]
      if left != right:
        break
      switches[value-idx-1], switches[value+idx-1] = ~left&1, ~right&1
      idx += 1

for op in operations:
  switch_operation(op)
for idx, s in enumerate(switches):
  if idx % 20 == 0 and idx != 0:
    print("")
  print(s, end=' ')
