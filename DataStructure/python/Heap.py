"""
힙.. 완전 이진 트리
여러 개의 값들 중 가장 큰 혹은 작은 값을 빠르게 찾아내도록 만들어진 자료구조
"""

data = [2, 5, 4, 8, 9, 3, 7, 3]

class Node:
  def __init__(self, data):
    self.data= data
    self.parent = None
    self.left = None
    self.right = None

  def setLeft(self, n):
    self.left = n
  def setRight(self, n):
    self.right = n

from collections import deque
class MaxHeap:
  def __init__(self):
    self.root = None
    self.last = None

  def _get_insert_position(self):
    if self.root is None:
      return None

    queue = deque([self.root])
    while queue:
      current = queue.popleft()
      if current.left is None or current.right is None:
        return current
      queue.append(current.left)
      queue.append(current.right)

  def _get_last_node(self):
    if self.root is None:
      return None
    if self.root == self.last:
      return self.root

    queue = deque([self.root])
    current = None
    while queue:
      current = queue.popleft()
      if current.left is not None:
        queue.append(current.left)
      if current.right is not None:
        queue.append(current.right)

    return current

  def _swap(self, node1, node2):
    node1.data, node2.data = node2.data, node1.data

  def insert(self, data):
    new_node = Node(data)

    if self.root is None:
      self.root = new_node
      self.last = new_node
      return

    parent = self._get_insert_position()
    new_node.parent = parent
    if parent.left is None:
      parent.left = new_node
    else:
      parent.right = new_node

    self.last = new_node
    self._heapify_up(self.last)

  def _heapify_up(self, node):
    while node.parent and node.parent.data < node.data:
      self._swap(node.parent, node)
      node = node.parent

  def extract(self):
    if self.root is None:
      return None

    result = self.root.data
    if self.root == self.last:
      self.root = None
      self.last = None
      return result

    last_node = self.last
    if last_node.parent:
      if last_node.parent.right == last_node:
        last_node.parent.right = None
      else:
        last_node.parent.left = None

    self.root.data = last_node.data
    self.last = self._get_last_node()
    self._heapify_down(self.root)

    return result

  def _heapify_down(self, node):
    while node:
      if node.right is None and node.left:
        largest = node.left
      elif node.left is None and node.right:
        largest = node.right
      elif node.right and node.left:
        largest = node.left if node.left.data > node.right.data else node.right
      else:
        break

      self._swap(largest, node)
      node = largest

  def print_heap(self):
    if self.root is None:
      return

    queue = deque([self.root])
    while queue:
      current = queue.popleft()
      print(current.data, end=" ")
      if current.left:
        queue.append(current.left)
      if current.right:
        queue.append(current.right)
    print()


if __name__ == "__main__":
  heap = MaxHeap()
  heap.insert(10)
  heap.insert(20)
  heap.insert(30)
  heap.insert(40)
  heap.insert(50)

  heap.print_heap()

  print('max extract: ', heap.extract())
  heap.print_heap()

