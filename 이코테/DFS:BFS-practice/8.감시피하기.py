# dfs 문제
from itertools import combinations
from xmlrpc.client import FastMarshaller
n = int(input())

board = []
teacher = []
space = []

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        # 2차원 배열의 위치를 넣는것은 append(i,j) or append((i,j))
        # 함수에 인자를 넣는게 아니면 ( ) 로 묶어서 보내야함. 그리고 queue에 넣는 파라미터는 () 로 두번 묶을 필요 없음
        if board[i][j] == 'T':
            teacher.append((i, j))
        if board[i][j] == 'X':
            space.append((i, j))


def watch(x, y, direction):
    # return 값을 주는 기준이?? 학생이 있으면 true, 함수의 마자막에 주는 return값은? 학생을 찾지 못한값
    # left
    if direction == 0:
        while y <= 0:
            if board[x][y] == 'T':
                return False
            if board[x][y] == 'S':
                return True
            y -= 1
    # right
    if direction == 1:
        while y > n:
            if board[x][y] == 'T':
                return False
            if board[x][y] == 'S':
                return True
            y += 1
    # up
    if direction == 2:
        while x <= 0:
            if board[x][y] == 'T':
                return False
            if board[x][y] == 'S':
                return True
            x -= 1
    # down
    if direction == 3:
        while y > n:
            if board[x][y] == 'T':
                return False
            if board[x][y] == 'S':
                return True
            x += 1
    return False


# process 부분
def process():
    for x, y in teacher:
        for i in range(4):
            # 학생을 찾았을떄 ( if문의 조건의 default는 True이다. )
            if watch(x, y, i) == True:
                return True
    return False


find = True

# point
for data in combinations(space, 3):
    for x, y in data:
        board[x][y] = 'O'
    # process 함수는 학생을 찾지못했단 return 값이 있다 따라서 울타리를 세웠을때, 이를 사용하면 된다
    if process():
        find = False
        break
    # 기존의 상태로 돌려줘야 한다.
    for x, y in data:
        board[x][y] = 'X'

if find == False:
    print('YES')
else:
    print('NO')
