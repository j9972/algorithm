# 수빈이가 동생을 찾는 가장 빠른 시간이니 bfs 문제이다
from collections import deque

# 각자의 위치
n, k = map(int, input().split())

# n,k의 범위가 100000이니까 그보다 큰값까지 범위를 둬야해서 +1
maxLength = 100001
board = [[] for _ in range(maxLength)]

# 그래프가 가능한 방법은 3가지 +1 -1 *2 ( 방향성이 3개 )
for i in range(maxLength):
    board[i] = [i+1, i-1, i*2]

visited = [0] * (maxLength)


def bfs(x):
    queue = deque([x])

    # 방문 처리가 0보다 크면 이미 방문한 상태
    if visited[x] > 0:
        return False

    # 시작점을 1로 만들어서 방문처리해준다
    visited[x] = 1

    while queue:
        now = queue.popleft()
        # for문 범위가 board[now]인 이유 -> board에서 위치가 +1 -1 *2 그걸 확인 하기 위해서
        for i in board[now]:
            if 0 <= i < maxLength and visited[i] == 0:
                visited[i] = visited[now] + 1
                queue.append(i)
        if now == k:
            # return 값이 이렇게 되는 이유 : 1씩 증가하는값을 보기 위함 처음에 1을 두어서 -1필요
            return visited[k] - 1

    return True


print(bfs(n))
