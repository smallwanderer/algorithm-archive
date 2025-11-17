# 백준 2268 수열의 합 7

import sys
input = sys.stdin.readline

class Fenwick:
  def __init__(self, array):
    self.n = len(array)
    self.tree = [0] * (self.n + 1)
    for i, x in enumerate(array):
      self.update(i+1, x)

  def _lastBit(self, num):
    return num & -num

  def _del_lastBit(self, num):
    return num & (num-1)

  # [0, n]의 범위 합을 구하는 함수
  def _sum(self, fenwick_bit):
    fenwick_sum = 0
    while fenwick_bit > 0:
      fenwick_sum += self.tree[fenwick_bit]
      fenwick_bit = self._del_lastBit(fenwick_bit)
    return fenwick_sum

  def update(self, fenwick_bit, diff):
    while fenwick_bit <= self.n:
      self.tree[fenwick_bit] += diff
      fenwick_bit += self._lastBit(fenwick_bit)

  def query(self, left, right):
    return self._sum(right) - self._sum(left-1)

n, m = map(int, input().split())
fenwick = Fenwick([0] * n)

for _ in range(m):
  op, a, b = map(int, input().split())
  if op == 0:
    if a > b:
        a, b = b, a
    sys.stdout.write(str(fenwick.query(a, b)) + '\n')
  else:
    diff = b - fenwick.query(a, a)
    fenwick.update(a, diff)
