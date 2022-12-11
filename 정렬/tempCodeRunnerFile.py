# #  세 용액
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()

# 절댓값은 작을수록 0에 가깝다는것을 이용해서 문제 풀기
# 투포인터 사용하기
s = 0
e = n-1
res = 3e9 + 1
ans = [0, 0, 0]

for i in range(n-2):
    while s < e:
        sumValue = data[s] + data[e] + data[i]

        if abs(sumValue) < res:
            res = min(res, abs(sumValue))
            ans = [data[s], data[i], data[e]]

            if res == 0:
                break
        if sumValue < 0:
            s += 1
        elif sumValue > 0:
            e -= 1
# while s < e:
#     m = (s+e) // 2
#     if s == m or e == m or s == e:
#         break

#     sumValue = data[s] + data[e] + data[m]

#     if abs(sumValue) < res:
#         res = min(res, abs(sumValue))
#         ans = [data[s], data[m], data[e]]

#         if res == 0:
#             break

#     if sumValue < 0:
#         s += 1
#     elif sumValue > 0:
#         e -= 1

ans.sort()
print(ans[0], ans[1], ans[2])
