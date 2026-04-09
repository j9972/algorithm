import sys
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    s,e = map(int,input().split())
    arr.append([s,e])


arr.sort(key=lambda x : (x[1],x[0]))

cnt = 1
cur = arr[0][1]

for i in range(1,len(arr)):
    #print(arr[i][0])
    s,e = arr[i][0], arr[i][1]

    if s >= cur:
        cnt += 1
        cur = e

print(cnt)

