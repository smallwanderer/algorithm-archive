class Archive_DFS:
    def __init__(self, start, graph):
        self.start = start
        self.graph = graph

    def neighbor(self, current):
        # 연결리스트인 경우
        return self.graph[current]

    # True if 찾았음 else False
    def search(self, end):
        graph = self.graph
        visited = [False] * len(graph)
        visited[self.start] = True

        stack = [self.start]
        while stack:
            current = stack.pop()
            if current == end:
                return True

            neighbors = self.neighbor(current=current)
            for neighbor in neighbors:
                if visited[neighbor]:
                    continue
                visited[neighbor] = True
                stack.append(neighbor)

        return False

# 사용 예시
if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1],
        4: [1, 5],
        5: [2, 4]
    }
    dfs = Archive_DFS(start=0, graph=graph)
    print(dfs.search(5))  # 출력: True

    print(dfs.search(6))  # 출력: False