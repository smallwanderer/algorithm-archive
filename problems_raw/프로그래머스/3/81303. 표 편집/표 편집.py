def solution(n, k, cmd):
    nodes = [True for _ in range(n)]  # 각 행이 살아있는지 여부
    prev = {i: i - 1 for i in range(n)}
    next = {i: i + 1 for i in range(n)}
    prev[0] = None
    next[n-1] = None
    
    current = k  # 현재 커서 위치
    stack = []  # 삭제된 행들을 저장

    for op in cmd:
        if op[0] == "D":  # 아래로 이동
            val = int(op[2:])
            for _ in range(val):
                current = next[current]
        
        elif op[0] == "U":  # 위로 이동
            val = int(op[2:])
            for _ in range(val):
                current = prev[current]
        
        elif op[0] == "C":  # 삭제
            stack.append((current, prev[current], next[current]))  # 삭제된 노드와 연결 정보 저장
            nodes[current] = False  # 삭제 처리

            if next[current] is not None:
                prev[next[current]] = prev[current]  # 다음 노드의 prev를 현재 노드의 prev로 변경
            if prev[current] is not None:
                next[prev[current]] = next[current]  # 이전 노드의 next를 현재 노드의 next로 변경

            current = next[current] if next[current] is not None else prev[current]  # 삭제 후 커서 이동
        
        elif op[0] == "Z":  # 복구
            rollback, prev_rollback, next_rollback = stack.pop()
            nodes[rollback] = True  # 복구 처리

            if prev_rollback is not None:
                next[prev_rollback] = rollback  # 복구된 노드를 이전 노드와 연결
            if next_rollback is not None:
                prev[next_rollback] = rollback  # 복구된 노드를 다음 노드와 연결

    # 최종 결과 생성
    result = "".join("O" if nodes[i] else "X" for i in range(n))
    return result
