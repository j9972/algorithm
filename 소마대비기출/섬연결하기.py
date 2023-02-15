# 42861 - 프로그래머스
# 크루스칼
def solution(n, costs):

    parent = [i for i in range(n+1)]

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    edges = []

    for i in costs:
        a, b, cost = i
        edges.append((cost, a, b))

    edges.sort()

    res = 0
    for i in edges:
        cost, a, b = i
        if find(a) != find(b):
            union(a, b)
            res += cost

    return res
