"""
Segment Tree (세그먼트 트리)
세그먼트 트리(Segment Tree)는 대규모 데이터 세트를 작은 세그먼트로 나누어 정렬하고 병합을 통해 빠르게 탐색하는 과정입니다.

세그먼트 트리는 다음과 같은 특징을 가집니다:
1. 각 노드는 특정 구간을 나타냅니다.
2. 루트 노드는 전체 구간을 나타내고, 자식 노드는 하위 구간을 나타냅니다.
3. 리프 노드는 원소 하나를 나타냅니다.
4. 내부 노드는 자식 노드의 값을 기반으로 계산된 값을 저장합니다.

세그먼트 트리의 주요 연산:
1. 업데이트 (Update): 특정 위치의 값을 변경
2. 쿼리 (Query): 특정 구간의 합, 최댓값, 최솟값 등을 계산

세그먼트 트리는 다음과 같은 경우에 유용합니다:
- 배열에서 특정 구간의 합을 빠르게 계산해야 할 때
- 배열에서 특정 구간의 최댓값/최솟값을 빠르게 계산해야 할 때
- 배열이 자주 변경되면서도 빠른 쿼리를 수행해야 할 때
"""

from Binary.CompleteBinary import CompleteBinaryTree

class SegmentTree(CompleteBinaryTree):
    def __init__(self, data):
        self.n = len(data)
        self.depth = 0
        self.init()
        super().__init__(self.size)
        self.build(data)

    def init(self):
        n = self.n
        # self.depth = self.n.bit_length()
        while (1 << self.depth) < n:
            self.depth += 1

        # Calculate size of the segment tree
        self.size = 1 << (self.depth + 1)

    def build(self, data):
        # Build the segment tree from the input data
        # Insert leaf nodes
        for i in range(self.n):
            self.tree[(1 << self.depth) + i] = data[i]
        # Build internal nodes
        for i in range((1 << self.depth) - 1, 0, -1):
            left = self.getLeftChild(i)
            right = self.getRightChild(i)
            self.tree[i] = (self.tree[left] if self.tree[left] is not None else 0) + \
                           (self.tree[right] if self.tree[right] is not None else 0)
    
    # Query the sum in the range [left, right)
    def query(self, left, right):
        left += (1 << self.depth)
        right += (1 << self.depth)
        result = 0

        while left < right:
            if left % 2 == 1:
                result += self.tree[left]
                left += 1
            if right % 2 == 1:
                right -= 1
                result += self.tree[right]
            left = self.getParent(left)
            right = self.getParent(right)

        return result
    
    # Query the sum of the range [left, right]
    def query2(self, left, right):
        left += (1 << self.depth)
        right += (1 << self.depth)
        result = 0

        while left <= right:
            if left % 2 == 1:
                result += self.tree[left]
                left += 1
            if right % 2 == 0:
                result += self.tree[right]
                right -= 1
            left = self.getParent(left)
            right = self.getParent(right)

        return result
    
    def update(self, index, value):
        # Update the value at index and propagate the change up the tree
        pos = index + (1 << self.depth)
        delta = value - self.tree[pos]
        self.tree[pos] += delta

        while pos > 1:
            pos = self.getParent(pos)
            left = self.getLeftChild(pos)
            right = self.getRightChild(pos)
            self.tree[pos] += delta

        return self.tree[1]  # Return the updated root value        

if __name__ == "__main__":
    data = [0, 1, 2, 3, 4, 5, 6, 7]
    seg_tree = SegmentTree(data)
    print(seg_tree.tree)

    # Query the sum from index [1, 5) (1 + 2 + 3 + 4)
    print(seg_tree.query(1, 5))  # Output: 10

    # Query the sum from index [0, 6] (0 + 1 + 2 + 3 + 4 + 5 + 6)
    print(seg_tree.query2(0, 6))  # Output: 21

    # Update index 3 to value 10
    seg_tree.update(3, 10)
    print(seg_tree.tree)