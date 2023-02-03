# 골드4 - 9663 - 다시
import sys
input = sys.stdin.readline
n = int(input())

res = 0
row = [0] * (n)


def promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x]-row[i]) == abs(x-i):
            return False
    return True


def dfs(queenCnt):
    global res
    if queenCnt == n:
        res += 1
    else:
        for i in range(n):
            # [queenCnt, i] 에 퀸을 놓겠다
            row[queenCnt] = i
            if promising(queenCnt):
                dfs(queenCnt+1)


dfs(0)
print(res)
