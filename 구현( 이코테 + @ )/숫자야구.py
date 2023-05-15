# 2503 실버3
import sys
input = sys.stdin.readline

n = int(input())

check = [True] * 1000

for i in range(123,1000):
    a = str(i)
    if a[0] == a[1] or a[2] == a[1] or a[2] == a[0]:
        check[i] = False
    if '0' in a:
        check[i] = False

for i in range(n):
    candidate, strike, ball = map(str, input().rstrip().split())

    for j in range(123,1000):
        s,b = 0,0
        for x in range(3):
            for y in range(3):
                if x==y and candidate[x] == str(j)[y]:
                    s += 1
                elif candidate[x] == str(j)[y]:
                    b += 1
        if int(strike) != s or int(ball) != b:
            check[j] = False

print(check[123:1000].count(True))