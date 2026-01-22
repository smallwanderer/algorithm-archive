"""
Lazy Segment Tree Implementation in Python
"""

from Segment import SegmentTree

class LazySegmentTree(SegmentTree):
    def __init__(self, data):
        super().__init__(data)
        self.lazy = [0] * self.size  # Lazy propagation array
    
    def _propagate(self, index, start, end):
        if self.lazy[index] != 0:
            # Update the current node
            self.tree[index] += (end - start) * self.lazy[index]
            if start + 1 < end:  # Not a leaf node
                left = self.getLeftChild(index)
                right = self.getRightChild(index)
                self.lazy[left] += self.lazy[index]
                self.lazy[right] += self.lazy[index]
            self.lazy[index] = 0
    
    def _update(self, index, start, end, l, r, value):
        if start >= r or end <= l:
            return
        self._propagate(index, start, end)
        if start >= l and end <= r:
            self.lazy[index] += value
            self._propagate(index, start, end)
            return
        
        mid = (start + end) // 2
        left = self.getLeftChild(index)
        right = self.getRightChild(index)
        self._update(left, start, mid, l, r, value)
        self._update(right, mid, end, l, r, value)
        self.tree[index] = self.tree[left] + self.tree[right]
    
    def updateRange(self, l, r, value):
        self._update(1, 0, 1 << self.depth, l, r, value)

    def _query(self, index, start, end, l, r):
        self._propagate(index, start, end)
        if start >= r or end <= l:
            return 0  # Neutral element for sum
        if start >= l and end <= r:
            return self.tree[index] # Return the sum for this segment
        
        mid = (start + end) // 2
        left = self.getLeftChild(index)
        right = self.getRightChild(index)
        left_sum = self._query(left, start, mid, l, r)
        right_sum = self._query(right, mid, end, l, r)
        return left_sum + right_sum
    
    def queryRange(self, l, r):
        return self._query(1, 0, 1 << self.depth, l, r)
    def update(self, index, value):
        # Update the value at index and propagate the change up the tree
        self._update(1, 0, 1 << self.depth, index, index + 1, value - self.queryRange(index, index + 1))