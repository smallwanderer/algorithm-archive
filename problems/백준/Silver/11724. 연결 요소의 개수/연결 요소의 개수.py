import sys

nodes_count, edges_count = map(int, sys.stdin.readline().split())
parent_node = {x+1 : x+1 for x in range(nodes_count)}

def find(node):
    root = node
    while parent_node[root] != root:
        root = parent_node[root]
        
    while node != root:
        parent = parent_node[node]
        parent_node[node] = root
        node = parent

    return root

def union(node1, node2):
  node1_root = find(node1)
  node2_root = find(node2)

  if node1_root != node2_root:
    parent_node[node1_root] = node2_root

for _ in range(edges_count):
  node1, node2 = map(int, sys.stdin.readline().split())
  union(node1, node2)

for i in range(1, nodes_count+1):
  find(i)

print(len(set(parent_node.values())))