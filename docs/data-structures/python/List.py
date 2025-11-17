class Node:
  def __init__(self, data):
    self.data = data

class List:
  def __init__(self, capacity=10):
    self.capacity = capacity
    self.ary = [None] * self.capacity
    self.size = 0

  def isEmpty(self):
    return self.size == 0

  def isFull(self):
    return self.size == self.capacity

  def expand_capacity(self):
    self.capacity *= 2
    new_ary = [None] * self.capacity
    for i in range(self.size):
      new_ary[i] = self.ary[i]
    self.ary = new_ary

  def normalize_index(self, pos):
    if pos < 0:
      pos += self.size
    return pos

  def getEntry(self, pos):
    pos = self.normalize_index(pos)
    return self.ary[pos].data

  def insert(self, index, e):
    if self.isFull():
      self.expand_capacity()

    self.size += 1
    normalized_index = self.normalize_index(index)

    for i in range(self.size-1, normalized_index, -1):
      self.ary[i] = self.ary[i - 1]
    self.ary[normalized_index] = Node(e)


  def delete(self, index):
    normalized_index = self.normalize_index(index)

    if self.isEmpty():
      raise ValueError("Underflow! List cannot be deleted")

    for i in range(normalized_index, self.size - 1):
      self.ary[i] = self.ary[i + 1]
    self.ary[self.size - 1] = None  # 마지막 요소 삭제
    self.size -= 1

  def replace(self, index, e):
    normalized_index = self.normalize_index(index)
    self.ary[normalized_index].data = e

  def __str__(self):
    return str([node.data for node in self.ary[:self.size] if node is not None])


if __name__ == "__main__":
  lst = List()

  # 초기 리스트 설정
  lst.insert(0, 1)
  lst.insert(1, 2)
  lst.insert(2, 3)
  lst.insert(3, 4)
  lst.insert(4, 5)
  print(lst)  # [1, 2, 3, 4, 5]

  print(lst.getEntry(3))  # 4

  lst.insert(2, 99)
  print(lst)  # [1, 2, 99, 3, 4, 5]

  lst.delete(1)
  print(lst)  # [1, 99, 3, 4, 5]

  lst.replace(2, 88)
  print(lst)  # [1, 99, 88, 4, 5]