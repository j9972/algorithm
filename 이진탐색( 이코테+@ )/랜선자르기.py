import sys
input = sys.stdin.readline

k,n = map(int,input().split())

line = []
for i in range(k):
    line.append(int(input()))

line.sort()

start = 1
end = max(line)
res = 0

while start <= end:
    tot = 0
    mid = (start+end) // 2

    for l in line:
        tot += l // mid
    
    if tot < n:
        end = mid - 1
    else:
        start = mid + 1
        res = mid

print(res)