# 실버 2 - 1182
# from itertools import combinations as cb
# import sys
# input = sys.stdin.readline

# n, s = map(int, input().split())
# data = list(map(int, input().split()))

# cnt = 0

# for i in range(1, n+1):
#     info = list(cb(data, i))
#     for j in info:
#         if sum(j) == s:
#             cnt += 1
# print(cnt)

# 백트래킹으로 푸는 문제
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
data = list(map(int, input().split()))

cnt = 0


def subsum(idx, subnum):
    global cnt
    if idx >= n:
        return
    subnum += data[idx]

    if subnum == s:
        cnt += 1

    subsum(idx+1, subnum)  # data[idx] 를 선택하는 경우
    subsum(idx+1, subnum - data[idx])  # data[idx] 를 선택하는 경우


subsum(0, 0)
print(cnt)
