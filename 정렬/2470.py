import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()

# 절댓값은 작을수록 0에 가깝다는것을 이용해서 문제 풀기

l = 0
r = n - 1

res = abs(data[l]+data[r])
final = [data[l], data[r]]

while l < r:
    lv = data[l]
    rv = data[r]

    sumv = lv + rv

    if abs(sumv) < res:
        res = abs(sumv)
        final = [lv, rv]

        if res == 0:
            break

    if sumv < 0:
        l += 1
    else:
        r -= 1
print(final[0], final[1])
