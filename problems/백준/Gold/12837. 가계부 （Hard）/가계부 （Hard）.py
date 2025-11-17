class Fenwick:
  def __init__(self, n):
    self.n = n
    self.tree = [0] * (self.n + 1)

  def update(self, bit, val):
    while bit <= self.n:
      self.tree[bit] += val
      bit += bit & (-bit)

  def sum(self, bit):
    sum = 0
    while bit > 0:
      sum += self.tree[bit]
      bit = bit & (bit - 1)
    return sum

  def query(self, left, right):
    return self.sum(right) - self.sum(left-1)

import sys
input = sys.stdin.readline

n, q = map(int, input().split())
fenwick = Fenwick(n)

for _ in range(q):
  a, b, c = map(int, input().split())
  if a == 1:
    fenwick.update(b, c)
  else:
    print(fenwick.query(b, c))