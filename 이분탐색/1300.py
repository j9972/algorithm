import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

a = [[1] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = (i+1)*(j+1)


b = sum(a, [])

b.sort()

print(b[k])


# 임의의 수 a보다 작거나 같은 수의 개수를 구하는 식이 존재한다.

# 각 행은 구구단처럼 1단 2단 3단... 식으로 나타나기 때문에 ( a / 행번호 ) 가 그 행에서 구하고자 하는 개수가 된다.

#    단, (a / 행번호) 가 N보다 클 경우에는 N이다.

start = 1
end = k
res = 0

while start <= end:
    mid = (start+end) // 2
    target = 0

    for i in range(1, n+1):
        target += min(n, mid//i)
    if target < k:
        start = mid + 1
    else:
        res = mid
        end = mid - 1

print(res)
