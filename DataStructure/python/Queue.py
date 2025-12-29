# implement of queue using List
import List

class Queue:
  def __init__(self, capacity=10):
    self.ary = List.List(capacity)
    self.front = 0
    self.rear = 0

  def isEmpty(self) -> bool:
    return self.rear == self.front

  def isFull(self) -> bool:
    return self.front == (self.rear+1) % self.ary.capacity

  # linear queue enqueue operation BigO takes O(n)
  # 이를 해결하기 위해 원형 큐로 설계. capacity 내에서 enqueue와 dequeue가 O(1)이 수행토록
  def enqueue(self, e):
    if self.isFull():
      self.ary.expand_capacity()

    self.ary.ary[self.rear] = List.Node(e)
    self.rear = (self.rear + 1) % self.ary.capacity

  def dequeue(self):
    if self.isEmpty():
      return None
    result = self.ary.getEntry(self.front)
    self.ary.ary[self.front] = None
    self.front = (self.front + 1) % self.ary.capacity
    return result

  def peek(self):
    if self.isEmpty():
      return None
    return self.ary.getEntry(self.front)

  def lookAry(self):
    instance_name = [name for name, obj in globals().items() if obj is self]
    instance_name = instance_name[0] if instance_name else "Unknown"
    if self.isEmpty():
      return "[]"

    if self.front < self.rear:
      return str([self.ary.getEntry(i) for i in range(self.front, self.rear)])
    else:
      first_part = [self.ary.getEntry(i) for i in range(self.front, self.ary.capacity)]
      second_part = [self.ary.getEntry(i) for i in range(0, self.rear)]

    print(f"{instance_name} array => {first_part + second_part}")

if __name__ == "__main__":
    q = Queue(5)  # 용량 5로 설정된 큐 생성

    # 데이터 삽입 (enqueue)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.ary.capacity)

    print(q.peek())  # 1

    q.lookAry()  # 현재 큐 상태 출력

    # 데이터 제거 (dequeue)
    q.dequeue()
    q.dequeue()

    print(q.peek())  # 3

    q.enqueue(5)
    q.enqueue(6)  # 원형 큐 특성상 rear가 다시 앞으로 이동

    q.lookAry()  # 현재 큐 상태 출력

    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()  # 모든 요소 제거

    q.lookAry()  # 비어 있는 상태 확인