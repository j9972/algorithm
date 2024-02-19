# 1차원 폭탄 떨어지고 아래로 떨어짐
n = int(input())

arr = [
    int(input())
    for _ in range(n)
]

out = [
    tuple(map(int,input().split()))
    for _ in range(2)
]

for i in out:
    s,e = i
    s -= 1
    e -= 1

    tmp = []

    for i in range(n):
        if s <= i <= e :
            continue
        else:
            tmp.append(arr[i])
    
    
    for i in range(n):
        if i >= len(tmp):
            arr[i] = 0
        else: arr[i] = tmp[i]
    
tmp = []
for i in arr:
    if i != 0:
        tmp.append(i)
    else:
        break

print(len(tmp))
for i in tmp:
    print(i)

        
    
    