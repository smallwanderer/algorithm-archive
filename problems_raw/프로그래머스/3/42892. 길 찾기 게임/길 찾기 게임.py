import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, val, h, idx):
        self.val = val
        self.h = h
        self.idx = idx
        self.top = None
        self.left = None
        self.right = None
        
class bTree:
    def __init__(self, node):
        self.root = node
        
    def insert(self, parent, node):
        if node.val < parent.val:
            if not parent.left:
                parent.left = node
                node.top = parent
            else:
                self.insert(parent.left, node)
        elif node.val > parent.val:
            if not parent.right:
                parent.right = node
                node.top = parent
            else:
                self.insert(parent.right, node)
        
    def preorder(self):
        result = []
        stack = [self.root]
        while stack:
            current = stack.pop()
            result.append(current.idx)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return result
    
    def postorder(self):
        result = []
        def _dfs(node, result):
            if node:
                _dfs(node.left, result)
                _dfs(node.right, result)
                result.append(node.idx)
        _dfs(self.root, result)
        return result
    
    def result(self):
        return [self.preorder(), self.postorder()]
        

def solution(nodeinfo):
    nodes = [Node(val, h, idx+1) for idx, (val, h) in enumerate(nodeinfo)]
    nodes.sort(key=lambda x: (-x.h, x.val))
    bt = bTree(nodes[0])
    for node in nodes[1:]:
        bt.insert(bt.root, node)
    
    return bt.result()
            
            
    
    
    
    