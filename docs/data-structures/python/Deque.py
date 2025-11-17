# deque(Double-End Queue)
class Deque:
  def __init__(self, capacity=10):
    self.capacity = capacity
    self.items = [None] * capacity
    self.front, self.rear = -1, -1

  def isEmpty(self) -> bool:
    if self.front == self.rear and not self.items[self.rear]:
      return True
    return False

  def isFull(self) -> bool:
    if self.front == self.rear and self.items[self.rear]:
      return True
    return False

  def addFront(self, e) -> bool:
    if not self.isFull():
      self.items[self.front] = e
      self.front = (self.front + self.capacity - 1) % self.capacity
      return True
    print("Unable to add element to deque")
    return False

  def deleteFront(self) -> bool:
    if not self.isEmpty():
      self.front = (self.front + 1) % self.capacity
      self.items[self.front] = None
      return True
    return False

  def getFront(self):
    if not self.isEmpty():
      return self.items[(self.front + 1) % self.capacity]
    return None

  def addRear(self, e) -> bool:
    if not self.isFull():
      self.rear = (self.rear + 1) % self.capacity
      self.items[self.rear] = e
      return True
    return False

  def deleteRear(self):
    if not self.isEmpty():
      self.items[self.rear] = None
      self.rear = (self.rear + self.capacity - 1) % self.capacity
      return True
    return False

  def getRear(self):
    return self.items[self.rear]

if __name__ == "__main__":
  dq = Deque(capacity=10)

  for i in range(9):
    if i%2==0: dq.addRear(i)
    else : dq.addFront(i)
  print(list(dq.items))

  print(dq.front, dq.rear)
  for i in range(2):
    print(f"{dq.getFront()} popped")
    dq.deleteFront()
  print(list(dq.items))
  for i in range(3):
    print(f"{dq.getRear()} popped")
    dq.deleteRear()
  print(list(dq.items))
  print(f"Where am i => front : {dq.getFront()}, rear : {dq.getRear()}")