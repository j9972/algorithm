# 실버 3 - 20920
import sys
input = sys.stdin.readline

n,m=map(int,input().split())
file = dict()

for i in range(n):
    s = input().rstrip()

    if len(s) < m:
        continue
    if file.get(s): # file.get()은 해당 값이 존재하면 값을 반환, 없으며 None
        file[s][0] += 1 # 존재하면 개수 증가
    else: # 존재하지 않으면 [개수, 길이, 단어] 추가
        file[s] = [1,len(s),s]

    
ans = sorted(file.items(), key=lambda x: (-x[1][0], -x[1][1], x[1][2]))

for i in ans:
    print(i[0])
