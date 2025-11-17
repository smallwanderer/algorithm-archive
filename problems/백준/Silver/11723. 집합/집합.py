class BitMasking:
  def __init__(self):
    self.bitset = 1 << 20

  def add(self, x):
    self.bitset = self.bitset | (1 << x)

  def remove(self, x):
    self.bitset = self.bitset & ~(1 << x)

  def check(self, x):
    sys.stdout.write(f"{1 if self.bitset & (1 << x) else 0}\n")

  def toggle(self, x):
    self.bitset = self.bitset ^ (1 << x)

  def all(self):
    self.bitset = (1 << 21) - 1

  def empty(self):
    self.bitset = 1 << 20

  def __str__(self):
    return f"{self.bitset:b}"

import sys
n = int(sys.stdin.readline().strip())
s = BitMasking()
operations = {'add': s.add, 'remove': s.remove, 'check': s.check, 'toggle': s.toggle, 'all': s.all, 'empty': s.empty}

for _ in range(n):
  op = sys.stdin.readline().strip().split()
  if len(op) == 1:
    operations[op[0]]()
  else:
    operations[op[0]](int(op[1])-1)