# dfs 영역 문제 -> 음료수 얼려 먹기
# done
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())

# 육지들의 높이를 나타냄
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

# 일정 높이 이하면 다 잠긴다
count = 1

# 알고리즘은 범위를 벗어나지 않고 수면 높이가 높으면서 방문하지 않은 곳을 돈다


def dfs(x, y, h):
    if 0 <= x < n and 0 <= y < n and board[x][y] > h and visited[x][y] == False:
        visited[x][y] = True
        dfs(x-1, y, h)
        dfs(x+1, y, h)
        dfs(x, y-1, h)
        dfs(x, y+1, h)
        return True
    return False


# h의 범위를 생각해 range를 갖고 가존의 최댓값을 비교하기 위해 cnt와 count 두 변수중 max로 큰값을 고른다
for i in range(1, 101):
    cnt = 0
    # board가 2차원 배열이므로 2차원으로 visited만들어 주기
    visited = [[False] * (n+1) for _ in range(n+1)]

    for a in range(n):
        for b in range(n):
            # 방문하지 않고 해수면 높이보다 높은 경우 체크
            if visited[a][b] == False and dfs(a, b, i) == True and board[a][b] > i:
                visited[a][b] = True
                cnt += 1
                dfs(a, b, i)
    count = max(cnt, count)
print(count)
