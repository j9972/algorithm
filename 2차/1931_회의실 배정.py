import sys
input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    s,e = map(int,input().split())
    arr.append([s,e])

last, cnt = 0,0

# key는 도착시간을 먼저 오름차순 하고 출발시간을 오름차순

for s,e in sorted(arr, key=lambda x : (x[1],x[0])):
    if s >= last:
        cnt += 1
        last = e
print(cnt)
