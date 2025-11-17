import collections

def solution(nodes, edges):
    # DSU (라벨 키 일관 사용)
    parent = {u: u for u in nodes}
    size = {u: 1 for u in nodes}
    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb: return
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]

    # 차수 집계 + 유니온
    cdedge = {u: 0 for u in nodes}
    for a, b in edges:
        union(a, b)
        cdedge[a] += 1
        cdedge[b] += 1

    # base = (노드홀짝 ⊕ 차수홀짝)
    base = {u: ((u & 1) ^ (cdedge[u] & 1)) for u in nodes}

    # 컴포넌트별 base=0/1 카운트
    cnt0 = collections.defaultdict(int)
    cnt1 = collections.defaultdict(int)
    roots = set()
    for u in nodes:
        r = find(u)
        roots.add(r)
        if base[u] == 0:
            cnt0[r] += 1
        else:
            cnt1[r] += 1

    # 정답
    answer = [0, 0]  # [atree, btree]
    for r in roots:
        if cnt0.get(r, 0) == 1:
            answer[0] += 1
        if cnt1.get(r, 0) == 1:
            answer[1] += 1
    return answer
