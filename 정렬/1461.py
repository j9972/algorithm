import sys
input = sys.stdin.readline

n, gap = map(int, input().split())
data = list(map(int, input().split()))

p = []
m = []
res = []
mv = 0

for d in data:
    if d > 0:
        p.append(d)
    else:
        m.append(d)

    if abs(d) > abs(mv):
        mv = d

p.sort(reverse=True)
m.sort()

for i in range(0, len(p), gap):
    if p[i] != mv:
        res.append(p[i])
for i in range(0, len(m), gap):
    if m[i] != mv:
        res.append(m[i])

cnt = abs(mv)
for r in res:
    cnt += abs(r) * 2
print(cnt)
# 출력
