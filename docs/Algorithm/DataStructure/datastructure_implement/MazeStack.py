# By Using Stack, we implement DFS(Depth First Search) Algorithm.
from implementation import Stack
import time

# '1' is wall, '0' is road. the start of the maze is 'e' and destination is 'x'
maze = [['1', '1', '1', '1', '1', '1', '1'],
        ['e', '0', '0', '0', '0', '0', '0'],
        ['1', '0', '1', '1', '0', '1', '1'],
        ['1', '0', '1', '0', '0', '0', 'x'],
        ['1', '0', '1', '0', '1', '1', '1'],
        ['1', '1', '1', '1', '1', '1', '1']]

maze_width, maze_depth = len(maze[0]), len(maze)
# the road taken should be True
simulation = maze[:]

def print_maze(maze):
  print("MAZE : ")
  for row in maze:
    print(row)
  print()

print_maze(simulation)
def DFS():
  global simulation

  def isValid(col, row):
    if 0 <= row < maze_width and 0 <= col < maze_depth:
      if simulation[col][row] == '0' or simulation[col][row] == 'x':
        return True
    return False

  print('dfs: ')
  stack = Stack.Stack()

  stack.push((1, 0))
  while not stack.isEmpty():
    time.sleep(1)
    current = stack.pop()
    if maze[current[0]][current[1]] == 'x':
      print_maze(simulation)
      print("MAZE DONE")
      return True

    simulation[current[0]][current[1]] = '2'
    print('current: ' , current, '=>', end='')

    direction = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1)}
    for dy, dx in direction.values():
      if isValid(current[0] + dx, current[1] + dy):
        stack.push((current[0] + dx, current[1] + dy))
    print("Current Stack: ", stack.items.ary)
    print_maze(simulation)

DFS()