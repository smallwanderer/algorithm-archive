"""
완전 이진 트리(Complete Binary Tree)

완전 이진 트리는 모든 레벨이 완전히 채워져 있고, 마지막 레벨에서는 왼쪽부터 노드가 채워지는 이진 트리입니다.
즉, 모든 노드가 왼쪽에서 오른쪽으로 순서대로 채워져 있어 균형 잡힌 구조를 유지합니다.
"""

class CompleteBinaryTree:
    def __init__(self, size):
        self.size = size
        self.tree = [None] * (size + 1)  # 1-based indexing
    
    def get(self, index):
        if index < 1 or index > self.size:
            return None
        return self.tree[index]
    
    def insert(self, value):
        for i in range(1, self.size + 1):
            if self.tree[i] is None:
                self.tree[i] = value
                return
        raise Exception("Tree is full")

    def getParent(self, index):
        if index <= 1 or index > self.size:
            return None
        return index // 2
    
    def getLeftChild(self, index):
        left_index = index * 2
        if left_index > self.size:
            return None
        return left_index
    
    def getRightChild(self, index):
        right_index = index * 2 + 1
        if right_index > self.size:
            return None
        return right_index

    