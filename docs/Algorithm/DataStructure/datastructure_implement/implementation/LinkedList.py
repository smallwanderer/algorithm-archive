class Node:
  """ 단일 연결 리스트의 노드 클래스 """
  def __init__(self, data):
    self.data = data
    self.next = None

# 연결리스트에서 첫 번째 노드의 주소를 저장하는 변수 헤드 포인터(Head Pointer)
# 파이썬에서는 포인터가 없는데..
class SinglyLinkedList:
  """ 단일 연결 리스트 구현 """
  def __init__(self):
    self.head = None
    self.length = 0

  def append(self, data):
    """ 리스트 끝에 노드 추가 """
    new_node = Node(data)
    self.length += 1

    if self.head is None:
      self.head = new_node
      return

    last = self.head
    while last.next:
      last = last.next
    last.next = new_node

  def _get_node(self, index):
    """ 주어진 인덱스의 노드를 반환하는 헬퍼 메서드 """
    if not (0 <= index < self.length):
      raise IndexError("Index out of range")

    current = self.head
    for _ in range(index):
      current = current.next
    return current

  def index(self, index):
    """ 인덱스에 해당하는 노드의 데이터 반환 """
    if index < 0:
      index += self.length
    return self._get_node(index).data

  def insert(self, index, data):
    """ 주어진 인덱스에 데이터 삽입 """
    if index >= self.length:
      raise IndexError("Index out of range")
    if index < 0:
      index += self.length

    new_node = Node(data)
    self.length += 1

    if index == 0:
      new_node.next = self.head
      self.head = new_node
      return

    prev_node = self._get_node(index-1)
    new_node.next = prev_node.next
    prev_node.next = new_node

  def remove(self, index):
    if index >= self.length:
      raise IndexError("Index out of range")
    if index < 0:
      index += self.length

    self.length -= 1

    if index == 0:
      self.head = self.head.next
      return

    prev_node = self._get_node(index-1)
    prev_node.next = prev_node.next.next

  def __str__(self):
    """ 리스트 모든 내용 출력 """
    result = []
    current = self.head
    while current:
      result.append(str(current.data))
      current = current.next
    return f"{result}"


if __name__ == '__main__':
  linkedList = SinglyLinkedList()
  linkedList.append('a')
  linkedList.append('b')
  linkedList.append('c')
  print(linkedList)  # a -> b -> c
  print("Length:", linkedList.length)

  print("Index 2:", linkedList.index(2))

  linkedList.insert(1, 'd')
  print(linkedList)  # a -> d -> b -> c

  linkedList.insert(0, 'e')
  print(linkedList)  # e -> a -> d -> b -> c

  linkedList.remove(1)
  print(linkedList)  # e -> d -> b -> c