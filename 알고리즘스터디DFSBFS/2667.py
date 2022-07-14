# dfs 전형적인 문제 - 음료수 얼려먹기

n = int(input())

board = []
for i in range(n):
    board.append(list(map(int, input())))

count = []
num = 0


def dfs(x, y):
    global num
    if 0 <= x < n and 0 <= y < n and board[x][y] == 1:
        board[x][y] = 0
        # 각 하나를 세어주기 위해 필요함
        num += 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


res = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            res += 1
            # 총 개수를 하나하나 보여주기 위해 하나의 배열에 넣어준다
            count.append(num)
            # 각 개수를 세기 위해서는 초기화 필수
            num = 0
count.sort()

print(res)
for i in range(len(count)):
    print(count[i])
