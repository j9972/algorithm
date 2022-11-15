import sys
input = sys.stdin.readline

n = int(input())
price = list(map(int, input().split()))
m = int(input())

d = [-float("inf") for _ in range(m+1)]

for i in range(n-1, -1, -1):
    p = price[i]
    for j in range(p, m+1):
        d[j] = max(d[j], i, d[j-p]*10+i)
        # i는 방번호ㅡ 숫자 d[j] -> 방번호, d[i] -> 가격
print(d[m])
