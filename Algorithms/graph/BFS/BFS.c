#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_VERTICES 100

typedef struct {
    int items[MAX_VERTICES];
    int front;
    int rear;
} Queue;

int isEmpty(Queue *q) {
    return q->front == q->rear;
}

int isFull(Queue *q) {
    return (q->rear + 1) % MAX_VERTICES == q->front;
}

void enqueue(Queue *q, int val) {
    if (isFull(q)) {
        printf("Queue is full\n");
        return;
    }
    q->items[q->rear] = val;
    q->rear = (q->rear + 1) % MAX_VERTICES;
}

int dequeue(Queue *q) {
    if (isEmpty(q)) {
        printf("Queue is empty\n");
        return -1;
    }
    int val = q->items[q->front];
    q->front = (q->front + 1) % MAX_VERTICES;
    return val;
}

void bfs(int graph[MAX_VERTICES][MAX_VERTICES], int start, int end) {
    bool visited[MAX_VERTICES] = {false};
    Queue q = {{0}, 0, 0};
    
    visited[start] = true;
    enqueue(&q, start);
    
    while (!isEmpty(&q)) {
        int vertex = dequeue(&q);
        if (vertex == end) {
            printf("Reached the end vertex: %d\n", end);
            return;
        }
        
        for (int i = 0; i < MAX_VERTICES; i++) {
            int neighbor = graph[vertex][i];
            if (neighbor == -1) break;
            
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                enqueue(&q, neighbor);
            }
        }
    }
    printf("End vertex %d not reachable from start vertex %d\n", end, start);
}

int main() {
    int graph[MAX_VERTICES][MAX_VERTICES] = {
        {1, 2, -1},
        {0, 3, 4, -1},
        {0, 4, -1},
        {1, -1},
        {1, 2, -1}
    };
    
    printf("BFS Traversal:\n");

    int start = 0;
    int end = 4;
    
    bfs(graph, start, end);
    
    return 0;
}