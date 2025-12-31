#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_VERTICES 100

typedef struct {
    int vertices[MAX_VERTICES];
    int top;
} Stack;

typedef struct {
    int adjacencyList[MAX_VERTICES][MAX_VERTICES];
    bool visited[MAX_VERTICES];
    int numVertices;
} Graph;

// 스택 초기화
void initStack(Stack *stack) {
    stack->top = -1;
}

// 스택에 값 추가
void push(Stack *stack, int value) {
    stack->vertices[++stack->top] = value;
}

// 스택에서 값 제거
int pop(Stack *stack) {
    stack->top--;
    return stack->vertices[stack->top + 1];
}

// 그래프 초기화
void initGraph(Graph *graph, int numVertices) {
    graph->numVertices = numVertices;
    for (int i = 0; i < numVertices; i++) {
        for (int j = 0; j < numVertices; j++) {
            graph->adjacencyList[i][j] = 0;
        }
        graph->visited[i] = false;
    }
}

// 간선 추가
void addEdge(Graph *graph, int u, int v) {
    graph->adjacencyList[u][v] = 1;
    graph->adjacencyList[v][u] = 1;
}

// DFS 함수
void dfs(Graph *graph, int startVertex, int endVertex) {
    Stack stack;
    initStack(&stack);
    
    push(&stack, startVertex);
    
    while (stack.top != -1) {
        int vertex = pop(&stack);

        if (graph->visited[vertex]) continue;
        graph->visited[vertex] = true;

        if (vertex == endVertex) {
            printf("Reached the end vertex: %d\n", endVertex);
            return;
        }

        for (int i = 0; i < graph->numVertices; i++) {
            if (graph->adjacencyList[vertex][i] && !graph->visited[i]) {
                push(&stack, i);
            }
        }
    }
}

// 메인 함수
int main() {
    Graph graph;
    initGraph(&graph, 5);
    
    // 간선 추가
    addEdge(&graph, 0, 1);
    addEdge(&graph, 0, 2);
    addEdge(&graph, 1, 3);
    addEdge(&graph, 2, 3);
    addEdge(&graph, 3, 4);
    
    printf("DFS 결과: ");
    dfs(&graph, 0, 4);
    printf("\n");
    
    return 0;
}