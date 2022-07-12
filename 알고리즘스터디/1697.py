# bfs문제 -> 거리차이를 좁히는데 최소 일수 -> done
from collections import deque

maxValue = 100001

# 0으로 방문을 초기화 시켜준다
visited = [0] * maxValue

n, k = map(int, input().split())

# 접근할 수 있는 방법을 얘기한다
board = [[] for _ in range(maxValue)]
for i in range(maxValue):
    board[i] = [i-1, i+1, i*2]


def bfs(x):
    queue = deque([x])

    if visited[x] > 0:
        return False
    visited[x] = 1

    while queue:
        now = queue.popleft()

        # 3가지 중에 있는지 체크
        for i in board[now]:
            # maxValue 안에 있고 방문하지 않은 조건을 먼저 찾는다
            if 0 <= i < maxValue and visited[i] == 0:
                # 카운트해준ㄷㅏ.
                visited[i] = visited[now] + 1
                queue.append(i)

        if now == k:
            # 도착했으면 값을 리턴해준다
            return visited[k] - 1

    return True


print(bfs(n))
