"""
Docstring for Algorithms.graph.BFS.impl.bfs

BFS(Breadth First Search, 너비 우선 탐색) 알고리즘은 시작 노드에서부터 인접 노드들을 순회한다.
거리(간수)가 1에서 시작하여 2 -> 3 -> ... 순으로 나아가는 구조를 가진다.

최단 거리 문제, 연결 요소 탐색, 레벨 기반 탐색 문제 등에서 사용한다.
"""
import collections

class Archive_BFS:
    def __init__(self, start, graph):
        self.start = start
        self.graph = graph
    
    def neighbor(self, current):
        # 연결리스트인 경우
        return self.graph[current]

    # True if 찾았음 else False
    def search(self, end):
        graph = self.graph
        visited = [False * len(graph)]

        queue = collections.deque([self.start])
        while queue:
            current = queue.popleft()
            if current == end:
                return True

            neighbors = self.neighbor(current=current)
            for neighbor in neighbors:
                if visited[neighbor]:
                    continue
                visited[neighbor] = True
                queue.append(neighbor)
        
        return False 
