from List import List, Node

class Stack:
  def __init__(self):
    self.items = List()
    self.capacity = 10
    self.size = 0

  def push(self, item):
    if self.size == self.capacity:
      self.items.expand_capacity()

    node = Node(item)
    self.items.insert(self.size, node)
    self.size += 1

  def pop(self):
    if self.size == 0:
      return None
    item = self.items.getEntry(self.size-1)
    self.items.delete(self.size-1)
    self.size -= 1
    return item

  def peek(self):
    if self.size == 0:
      return None
    print(self.items.getEntry(self.size-1))
    return self.items.getEntry(self.size-1)

if __name__ == '__main__':
  stack = Stack()
  stack.push(1)
  stack.push(2)
  stack.peek()
  stack.pop()
  stack.peek()
  stack.push(5)
  stack.peek()