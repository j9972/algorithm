from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def move_robot(pos, board):
    pos_list = []  # 로봇이 이동가능한 좌표들 담을 리스트
    # 현재 로봇 위치 좌표 값
    pos = list(pos)
    pos_x1, pos_y1, pos_x2, pos_y2 = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    for i in range(4):
        pos_next_x1, pos_next_y1, pos_next_x2, pos_next_y2 = pos_x1 + dx[i], pos_y1 + dy[i], pos_x2 + dx[i], pos_y2 + \
            dy[i]
        # 로봇의 좌표에 있는 값들이 모두 0일 경우에는 이동 가능
        if board[pos_next_x1][pos_next_y1] == 0 and board[pos_next_x2][pos_next_y2] == 0:
            pos_list.append({(pos_next_x1, pos_next_y1),
                            (pos_next_x2, pos_next_y2)})
    # 3-2.회전하는 경우
    # 3-2-1. 로봇이 가로로 있는 경우(로봇의 두 좌표 x값이 같을 때)
    if pos_x1 == pos_x2:
        # 위(-1), 아래(+1) 이동하는 경우
        for i in [-1, 1]:
            if board[pos_x1 + i][pos_y1] == 0 and board[pos_x2 + i][pos_y2] == 0:
                pos_list.append({(pos_x1, pos_y1), (pos_x1 + i, pos_y1)})
                pos_list.append({(pos_x2, pos_y2), (pos_x2 + i, pos_y2)})
    # 3-2-2. 로봇이 세로로 있는 경우(로봇의 두 좌표 y값이 같을 때)
    elif pos_y1 == pos_y2:
        # 왼쪽(-1), 오른쪽(+1) 이동하는 경우
        for i in [-1, 1]:
            if board[pos_x1][pos_y1 + i] == 0 and board[pos_x2][pos_y2 + i] == 0:
                pos_list.append({(pos_x1, pos_y1), (pos_x1, pos_y1 + i)})
                pos_list.append({(pos_x2, pos_y2), (pos_x2, pos_y2 + i)})
    # 로봇이 갈 수 있는 위치 좌표 리스트 return
    return pos_list


def solution(board):
    # 1. 맵 길이를 늘리기
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    robot_queue = deque([])  # 로봇 좌표와 시간을 담는 큐 정의
    visited = []  # 로봇이 거쳐간 맵 좌표들 기록(방문 처리용 리스트)
    # 로봇의 초기 위치 정보 넣기
    pos = {(1, 1), (1, 2)}
    robot_queue.append((pos, 0))
    visited.append(pos)
    # 큐가 빌 때까지 BFS 탐색
    while robot_queue:
        pos, cost = robot_queue.popleft()
        # 로봇 위치 좌표 중 하나가 (n, n) 좌표에 도달했다면 종료
        if (n, n) in pos:
            return cost
        # 큐에서 꺼낸 로봇 위치에서 갈 수 있는 곳 탐색
        for next_pos in move_robot(pos, new_board):
            if next_pos not in visited:
                visited.append(next_pos)
                robot_queue.append((next_pos, cost + 1))
    return cost


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [
      0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
