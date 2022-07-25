import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int, input().split())


res = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_va = min(data)
    # 가장 작은 수중에서 가장 큰 값 찾기
    res = max(res, min_va)
print(res)


# new way -> 게임 전략을 잘 파악 해야한다
# n, m = map(int, input().split())

# board = []
# v = []
# for i in range(n):
#     board = list(map(int, input().split()))
#     v.append(min(board))
# print(max(v))
