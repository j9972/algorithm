from itertools import combinations as cb
n = int(input())

ans = []

for i in range(1,11): # 몇자리 만들거야?
    for j in cb(range(10), i): # 어떤 수들로 만들거야
        j_list = sorted(list(j), reverse=True) # 감소하는 수로 만들어
        ans.append(int("".join(map(str, j_list)))) # 타입 list -> str -> int

    
ans.sort()

if len(ans) > n:
    print(ans[n])
else:
    print(-1)

