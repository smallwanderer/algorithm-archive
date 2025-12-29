import Queue
arrayTree = [1, 2, 3, 4, None, None, 5, 6, 7, None, None, None, None, None, 8]

class Tnode:
  def __init__(self, data, left, right):
    self.data = data
    self.left = left
    self.right = right

class BinaryTree:
  def __init__(self, data):
    self.root = data

  def insert(self, data):
    pass


  def preorder(self, node):
    if node is not None:
      print(node.data, end=' ')
      self.preorder(node.left)
      self.preorder(node.right)

  def inorder(self, node):
    if node is not None:
      self.inorder(node.left)
      print(node.data, end=' ')
      self.inorder(node.right)

  def postorder(self, node):
    if node is not None:
      self.postorder(node.left)
      self.postorder(node.right)
      print(node.data, end=' ')

  def levelOrder(self, node):
    queue = Queue.Queue()
    queue.enqueue(node)
    while not queue.isEmpty():
      n = queue.dequeue()
      if n != None:
        print(n.data, end=' ')
        queue.enqueue(n.left)
        queue.enqueue(n.right)

  def count_node(self, n):
    if n == None:
      return 0
    else:
      return 1 + self.count_node(n.left) + self.count_node(n.right)

  # leaf node(단말 노드)는 자식 노드가 없는 노드를 의미
  def count_leaf(self, n):
    if n == None:
      return 0
    if n.left == None and n.right == None:
      return 1
    else:
      return self.count_leaf(n.left) + self.count_leaf(n.right)

  def count_height(self, n):
    if n == None:
      return 0
    return 1+max(self.count_height(n.left), self.count_height(n.right))


if __name__ == "__main__":
  d = Tnode('D', None, None)
  e = Tnode('E', None, None)
  b = Tnode('B', d, e)
  f = Tnode('F', None, None)
  c = Tnode('C', f, None)
  a = Tnode('A', b, c)
  bt = BinaryTree(a)

  print("inorder: ", end='')
  bt.inorder(a)
  print("preorder: ", end='')
  bt.preorder(a)
  print("postorder: ", end='')
  bt.postorder(a)
  print("levelorder: ", end='')
  bt.levelOrder(a)

  print()
  print(" 노두 개수 : ", bt.count_node(a))
  print(" 단말 개수 : ", bt.count_leaf(a))
  print(" 트리 높이 : ", bt.count_height(a))