n = int(input())

d = [0] * 101

for _ in range(n):
    idx, alpha = input().split()

    if alpha == 'H':
        d[int(idx)] = -1
    else:
        d[int(idx)] = 1

cnt = 0
for i in range(101):
    for j in range(i+1, 101):
        if d[i] != 0 and d[j] != 0:
            cnt1, cnt2 = 0,0

            for k in range(i,j+1):
                if d[k] == -1:
                    cnt1 += 1
                elif d[k] == 1:
                    cnt2 += 1
                
            if cnt1 == 0 or cnt2 == 0 or cnt1 == cnt2:
                cnt = max(cnt, abs(j-i))
print(cnt)
