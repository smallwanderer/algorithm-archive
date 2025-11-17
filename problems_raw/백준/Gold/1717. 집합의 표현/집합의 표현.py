# Disjoint Set
import sys
sys.setrecursionlimit(1000000)

def find(node):
  if parent[node] != node:
    parent[node] = find(parent[node])
  return parent[node]

def union(node1, node2):
  node1_root = find(node1)
  node2_root = find(node2)

  if node1_root != node2_root:
    parent[node1_root] = node2_root

def expression_of_set(operation, a, b):
  if operation == 0:
    union(a, b)
  else:
    print("YES" if find(a) == find(b) else "NO")

n, m = map(int, sys.stdin.readline().split())
parent = {x : x for x in range(n+1)}
for _ in range(m):
  op, a, b = map(int, sys.stdin.readline().split())
  expression_of_set(op, a, b)