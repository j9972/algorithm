# 골드4 - 1043 ( 분리집합 ) -> 다시
# 알고있는 사람의 수가 중요한것이 아니다
import sys
input = sys.stdin.readline

n, m = map(int, input().split())


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    b = find(b)
    a = find(a)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


parent = [i for i in range(n+1)]
KNOW_TRUTH = 0

# 진실을 아는 사람의 번호
true = list(map(int, input().split()))[1:]
for person in true:
    parent[person] = KNOW_TRUTH

res = 0
party = []
for i in range(m):
    data = list(map(int, input().split()))[1:]
    for i in range(len(data)-1):
        union(data[i], data[i+1])
    party.append(data)

for p in party:
    know = False
    for i in range(len(p)):
        if find(p[i]) == KNOW_TRUTH:
            know = True
            break
    if not know:
        res += 1
print(res)
