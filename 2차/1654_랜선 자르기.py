import sys
input = sys.stdin.readline

k, n = map(int,input().split())

line = []
for _ in range(k):
    line.append(int(input()))

line.sort()
start, ans = 1,0
end = max(line)

while start <= end:
    tot = 0
    mid = (start + end) // 2

    for i in line:
        tot += i // mid
    
    if tot < n :
        end = mid - 1
    else:
        ans = mid
        start = mid + 1

print(ans)
