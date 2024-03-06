n = int(input())

lines = list()
for i in range(n):
    s,e = map(int,input().split())
    lines.append((s,e))

lines.sort(key = lambda x : x[1])

cnt = 1
cur_idx = lines[0][1]
for i in range(1,n):
    if lines[i][0] > cur_idx:
        cnt += 1
        cur_idx = lines[i][1]
print(cnt)