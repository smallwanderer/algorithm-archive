height, width, start_y, start_x, operations = map(int, input().split())

top, N, E = 1, 2, 3
direction = {3: (-1, 0), 4: (1, 0), 1: (0, 1), 2:(0, -1)}
dice = [0 for _ in range(7)]
world = [list(map(int, input().split())) for _ in range(height)]
operation = list(map(int, input().split()))

def move_dice(operation):
  global top, N, E
  if operation[0] == 1:
    top, N = N, 7-top
  if operation[0] == -1:
    top, N, = 7-N, top
  if operation[1] == -1:
    top, E = E, 7-top
  if operation[1] == 1:
    top, E = 7-E, top

current = (start_y, start_x)
for op in operation:
  # print(direction[op], current)
  dy, dx = direction[op]
  ny, nx = current[0] + dy, current[1] + dx
  if not (0 <= ny < height and 0 <= nx < width):
    # print(op, 'unable!')
    continue
  move_dice(direction[op])
  if world[ny][nx] == 0:
    world[ny][nx] = dice[7-top]
  else:
    dice[7-top] = world[ny][nx]
    world[ny][nx] = 0
  current = (ny, nx)
  # print(f"top : {top}, North : {N}, East : {E}")
  # print("dice:", dice[1:])
  print(dice[top])

