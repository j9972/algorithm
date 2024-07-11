n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

max_cnt = 0

for i in range(n):
    for j in range(n-2):
        max_cnt = max(max_cnt, sum(arr[i][j:j+3]))
print(max_cnt)