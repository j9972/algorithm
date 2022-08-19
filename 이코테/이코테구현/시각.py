# N 입력받기
n = int(input())

count = 0
for i in range(n+1):
    for j in range(60):
        for h in range(60):
            if '3' in str(i) + str(j) + str(h):
                count += 1
print(count)
