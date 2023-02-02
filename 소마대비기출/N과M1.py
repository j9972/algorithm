# 실버 3 - 15649 - 다시
# from itertools import permutations as pm
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# num = []
# for i in range(n):
#     num.append(i+1)

# data = list(pm(num, m))

# for i in data:
#     for j in i:
#         print(j, end=' ')
#     print()
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
res = []


def dfs(num):
    if num == m:
        print(' '.join(map(str, res)))
        return
    else:
        for i in range(1, n+1):
            if i not in res:
                res.append(i)
                dfs(num+1)
                res.pop()


dfs(0)
