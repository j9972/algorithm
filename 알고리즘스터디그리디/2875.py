import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

# 대회 남1 여2 , 인턴쉽 k 명
total = n + m - k
teamCount = (total - (total % 3))//3

if n//2 < teamCount or m < teamCount:
    if n//2 > m:
        print(m)
    else:
        print(n//2)
else:
    print(teamCount)
