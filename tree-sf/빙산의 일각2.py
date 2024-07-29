n = int(input())

arr = [
    int(input())
    for _ in range(n)
]

max_cnt = 0

for h in range(1,1001):
    flag = False
    cnt = 0
    for i in range(n):
        if arr[i] - h > 0:
            if not flag:
                cnt += 1
                flag = True
        else:
            flag = False

    max_cnt = max(max_cnt ,cnt)

print(max_cnt)


for h in range(1,1001):
    flag = False
    cnt = 0
    for i in range(n):
        if arr[i] - h > 0:
            if not flag:
                cnt += 1
                flag = True
        else:
            flag = False

    max_cnt = max(max_cnt ,cnt)

print(max_cnt)