import sys

parent_network = dict()
network_size = dict()

# Finding Root of Node
def find(node):
  if parent_network[node] != node:
    parent_network[node] = find(parent_network[node])
  return parent_network[node]

# Union of Roots
def union(node1, node2):
  node1_root = find(node1)
  node2_root = find(node2)

  if node1_root != node2_root:
    parent_network[node1_root] = node2_root
    network_size[node2_root] += network_size[node1_root]

  return network_size[node2_root]

def friend_network():
  network_insertion = int(sys.stdin.readline())

  for i in range(network_insertion):
    a, b = sys.stdin.readline().split()
    # Disjoint node 생성
    for p in (a, b):
      if p not in parent_network:
        parent_network[p] = p
        network_size[p] = 1

    # Union-Find
    print(union(a, b))

testcase = int(sys.stdin.readline())
for _ in range(testcase):
  friend_network()
  parent_network = dict()
  network_size = dict()