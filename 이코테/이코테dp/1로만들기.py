x = int(input())  # 사용자로부터 받는 입력값

d = [0] * 30001  # 30001은 범위의 max + 1

for i in range(2, x+1):
    d[i] = d[i-1] + 1
    if d[i] % 2 == 0:
        d[i] = d[i//2] + 1
    elif d[i] % 3 == 0:
        d[i] = d[i//3] + 1
    elif d[i] % 5 == 0:
        d[i] = d[i//5] + 1

print(d[x])
