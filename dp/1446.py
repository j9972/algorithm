import sys
input = sys.stdin.readline

n, d = map(int, input().split())

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

data = sorted(data, key=lambda x: (x[0], x[1], x[2]))
D = [i for i in range(d+1)]

for i in data:
    s, e, sD = i
    if e <= d:
        D[e] = min(D[s]+sD, D[e])
    # 지름길 업데이트 해주는 코드 e부터 d까지 1씩 전진하면서 최소값을 업데이터 한다
    for k in range(s, d+1):
        D[k] = min(D[k], D[k-1]+1)

print(D[d])
