import copy
import sys
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

data = [[None]*4 for _ in range(4)]
for i in range(4):
    info = list(map(int, input().split()))
    for j in range(4):
        data[i][j] = [info[j*2], info[j*2+1]-1]


def turning(direction):
    return (direction+1) % 8


def finding(array, index):
    for x in range(4):
        for y in range(4):
            if array[x][y][0] == index:
                return (x, y)
    return None


def moving(array, now_x, now_y):
    for i in range(1, 17):
        pos = finding(array, i)

        if pos != None:
            x, y = pos[0], pos[1]
            direction = array[x][y][1]
            for _ in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]

                if 0 <= nx < 4 and 0 <= ny < 4:
                    if not (nx == now_x and ny == now_y):
                        array[x][y][1] = direction
                        array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
                        break
                direction = turning(direction)


def eating(array, x, y):
    posList = []
    direction = array[x][y][1]

    for i in range(4):
        x += dx[direction]
        y += dy[direction]

        if 0 <= x < 4 and 0 <= y < 4:
            if array[x][y][0] != -1:
                posList.append((x, y))
    return posList


res = 0


def dfs(array, x, y, tot):
    global res
    array = copy.deepcopy(array)

    tot += array[x][y][0]
    array[x][y][0] = -1

    moving(array, x, y)
    pos = eating(array, x, y)

    if len(pos) == 0:
        res = max(res, tot)
        return

    for next_x, next_y in pos:
        dfs(array, next_x, next_y, tot)


dfs(data, 0, 0, 0)
print(res)
