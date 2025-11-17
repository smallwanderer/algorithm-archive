from implementation import Queue
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


def BFS():
  queue = Queue.Queue()
  global simulation
  queue.enqueue((1, 0))

  while not queue.isEmpty():
    time.sleep(1)
    col, row = queue.dequeue()
    if maze[col][row] == 'x':
        print_maze(simulation)
        print("BFS DONE")
        return True

    simulation[col][row] = '2'

    def isValid(col, row):
      if 0 <= col < maze_depth and 0 <= row < maze_width:
        if simulation[col][row] == '0' or simulation[col][row] == 'x':
          return True
      return False

    directions = {'up': (1, 0), 'down': (-1, 0), 'left': (0, -1), 'right': (0, 1)}
    for dy, dx in directions.values():
      if isValid(col + dy, row + dx):
        queue.enqueue((col + dy, row + dx))

    print(f"current step : {(col, row)} => {queue.ary}")
    print_maze(simulation)
  return False

BFS()
