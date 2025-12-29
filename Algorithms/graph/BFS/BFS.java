import java.util.*;

public class BFS {
    private int vertices;
    private List<List<Integer>> adjacencyList;
    
    // 생성자
    public BFS(int vertices) {
        this.vertices = vertices;
        this.adjacencyList = new ArrayList<>();
        for (int i = 0; i < vertices; i++) {
            adjacencyList.add(new ArrayList<>());
        }
    }
    
    // 간선 추가
    public void addEdge(int u, int v) {
        adjacencyList.get(u).add(v);
    }
    
    // BFS 구현
    public void bfs(int startVertex, int endVertex) {
        boolean[] visited = new boolean[vertices];
        Queue<Integer> queue = new LinkedList<>();
        
        visited[startVertex] = true;
        queue.add(startVertex);
        
        while (!queue.isEmpty()) {
            int currentVertex = queue.poll();
            if (currentVertex == endVertex) {
                System.out.println("도착 노드 " + endVertex + "에 도달했습니다.");
                return;
            }
            System.out.print(currentVertex + " ");
            
            // 인접한 모든 노드 탐색
            for (int neighbor : adjacencyList.get(currentVertex)) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    queue.add(neighbor);
                }
            }
        }
    }
    
    public static void main(String[] args) {
        BFS graph = new BFS(5);
        graph.addEdge(0, 1);
        graph.addEdge(0, 2);
        graph.addEdge(1, 3);
        graph.addEdge(2, 3);
        graph.addEdge(3, 4);
        
        System.out.println("BFS 결과:");
        graph.bfs(0, 4);
    }
}