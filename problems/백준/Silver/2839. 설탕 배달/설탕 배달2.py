mport sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import util

n = int(input())

def sugar_delivery(n):
  result = 0

  while True:
    if n < 0:
      return -1
    if n % 5 == 0:
      result += n // 5
      return result
    n -= 3
    result += 1

util.time_calculator(sugar_delivery, n)
print(suger_delivery(n))
