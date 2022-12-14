from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

data = [[0]*(n+1) for _ in range(n+1)]

k_list = []
for _ in range(k):
    x, y = map(int, input().split())
    k_list.append([x, y])

for i in range(len(k_list)):
    data[k_list[i][0]][k_list[i][1]] = 1

# print(data)
L = int(input())
direction = []
for i in range(L):
    t, d = map(str, input().split())
    direction.append([int(t), d])

# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


# direction == 방향에대한 숫자 ( 동남서북 0,1,2,3 ) , c == 방향 ( 왼쪽, 오른쪽만 취급 )
# %4 를 해주는 이유는 4이상 0 미만되는것을 방지
def turing(direction, c):
    if c == 'L':
        direction = (direction-1) % 4
    else:
        direction = (direction+1) % 4
    return direction


def process():

    q = deque()
    x, y = 1, 1
    q.append([x, y])
    data[x][y] = 2  # 방문 처리

    cnt = 0
    direct = 0

    # 여 부분
    index = 0

    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]

        if 1 <= nx <= n and 1 <= ny <= n and data[nx][ny] != 2:
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append([nx, ny])
                px, py = q.popleft()
                data[px][py] = 0
            elif data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append([nx, ny])
        else:
            cnt += 1
            break
        cnt += 1
        x, y = nx, ny

        if index < L and direction[index][0] == cnt:
            direct = turing(direct, direction[index][1])
            index += 1
    return cnt


print(process())
