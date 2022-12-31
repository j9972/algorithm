n, m = map(int, input().split())
data = []
for i in range(n):
    info = list(map(int, input().split()))
    data.append(min(info))
print(max(data))
