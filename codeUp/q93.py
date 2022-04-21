n = int(input())
data = list(map(int, input().split()))

a = data[0]

for i in data:
    if i < a:
        a = i
print(a)
