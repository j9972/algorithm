from itertools import combinations as cb
import sys
input = sys.stdin.readline

home = []
chicken = []

n, m = map(int, input().split())

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            home.append((i, j))
        elif data[j] == 2:
            chicken.append((i, j))

distance = 1e9
for ch in cb(chicken, m):
    res = 0  # 중간 점검을 위한 길이
    for hx, hy in home:
        ch_len = 1e9  # 가장 가까운 치킨집 찾기
        for i in range(m):
            ch_len = min(ch_len, abs(hx - ch[i][0]) + abs(hy - ch[i][1]))
        res += ch_len  # 가장 가까운 치킨집 거리 더하기
    distance = min(distance, res)
print(distance)
