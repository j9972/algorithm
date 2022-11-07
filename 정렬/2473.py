# #  세 용액
# import sys
# input = sys.stdin.readline

# n = int(input())
# data = list(map(int, input().split()))
# data.sort()

# # 절댓값은 작을수록 0에 가깝다는것을 이용해서 문제 풀기


# for i in range(n-2):
#     l = 0
#     r = n - 1

#     res = abs(data[l]+data[i]+data[r])
#     final = [data[l], data[i], data[r]]

#     while l < r:
#         lv = data[l]
#         rv = data[r]
#         mv = data[i]

#         sumv = lv + rv + mv

#         if abs(sumv) < res:
#             res = abs(sumv)
#             final = [lv, mv, rv]

#             if res == 0:
#                 print(final[0], final[1], final[2])
#                 break

#         if sumv < 0:
#             l += 1
#         else:
#             r -= 1

# print(final[0], final[1], final[2])

from itertools import permutations

numbers = [3, 30, 34, 5, 9]


def solution(numbers):
    res = list(permutations(numbers, len(numbers)))
    ans = []

    for i in range(len(res)):
        ans.append(''.join(str(s) for s in res[i]))

    print(max(ans))


solution(numbers)
