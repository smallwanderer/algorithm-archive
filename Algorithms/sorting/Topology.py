"""
위상 정렬(Topology Sorting)은 방향이 있는 그래프의 선형적인 순서를 찾는 알고리즘입니다.
이는주로 작업 스케줄링, 의존성 문제, 순서 결정 문제등에 사용됩니다.

위상 정렬은 다음과 같은 특징을 가집니다:
1. 방향 그래프(DAG, Directed Acyclic Graph)에서만 적용 가능합니다.
2. 그래프의 모든 간선을 따라 정점들이 선형적으로 정렬됩니다.
3. 여러 개의 올바른 위상 정렬이 존재할 수 있습니다.

알고리즘:
1. 진입 차수 계산: 각 정점의 진입 차수를 계산
2. 진입 차수가 0인 정점 큐에 추가: 진입 차수가 0인 모든 정점을 큐에 넣습니다.
3. 큐에서 정점 제거 및 결과에 추가: 제거된 정점의 인접 정점들의 차수를 감소시키고, 진입 차수가 0이 된 정점을 큐에 추가합니다.
4. 반복: 큐가 빌 때까지 2-3단계를 반복합니다.
이 알고리즘은 그래프의 모든 정점을 방문할 때까지 반복되며, 최종적으로 위상 정렬된 순서를 반환합니다.
"""

from collections import deque, defaultdict

class TopologySort:
    def kahn(self, vertex, edges):
        graph = defaultdict(list)
        indegree = [0] * vertex 

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        queue = deque([i for i in range(vertex) if indegree[i] == 0])
        result = []

        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(result) != vertex:
            return []  # 사이클이 존재하여 위상 정렬 불가능
        
        return result

    def dfs(self, vertex, edges):
        visited = [0] * vertex
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
        
        def dfs_util(node):
            visited[node] = 1
            for neighbor in graph[node]:
                if visited[neighbor] == 0:
                    dfs_util(neighbor)
                elif visited[neighbor] == 1:
                    raise ValueError("Graph is not a DAG; cycle detected")
            visited[node] = 2
            result.append(node)

        result = []
        for i in range(vertex):
            if not visited[i]:
                dfs_util(i)
        return result[::-1]


if __name__ == "__main__":
    vertex = 6
    edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
    
    topo_sort = TopologySort()
    
    print("Kahn's Algorithm Result:")
    try:
        result_kahn = topo_sort.kahn(vertex, edges)
        print(result_kahn)
    except Exception as e:
        print(e)
    
    print("DFS-based Algorithm Result:")
    try:
        result_dfs = topo_sort.dfs(vertex, edges)
        print(result_dfs)
    except Exception as e:
        print(e)