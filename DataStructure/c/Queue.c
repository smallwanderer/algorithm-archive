# include <stdio.h>
# include <stdlib.h>
# define MAX_QUEUE_SIZE 100

typedef struct {
    int items[MAX_QUEUE_SIZE];
    int front;
    int rear;
} Queue;

void initQueue(Queue *q) {
    q->front = 0;
    q->rear = 0;
}

int isQueueEmpty(Queue *q) {
    return q->front == q->rear;
}

int isQueueFull(Queue *q) {
    return (q->rear + 1) % MAX_QUEUE_SIZE == q->front;
}

int enqueue(Queue *q, int value) {
    if (isQueueFull(q)) {
        printf("Queue is full\n");
        return 0;
    }
    q->items[q->rear] = value;
    q->rear = (q->rear + 1) % MAX_QUEUE_SIZE;
    return 1;
}

int dequeue(Queue *q) {
    if (isQueueEmpty(q)) {
        printf("Queue is empty\n");
        return -1;
    }

    int value = q->items[q->front];
    q->front = q->front + 1 % MAX_QUEUE_SIZE;
    return value;
}

int main() {
    Queue q;
    initQueue(&q);
    // Queue 사용 예제

    enqueue(&q, 10);
    enqueue(&q, 20);
    enqueue(&q, 30);

    printf("Dequeued: %d\n", dequeue(&q));
    printf("Dequeued: %d\n", dequeue(&q));

    enqueue(&q, 40);
    printf("Dequeued: %d\n", dequeue(&q));
    printf("Dequeued: %d\n", dequeue(&q));
}

