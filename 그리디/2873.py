import sys
input = sys.stdin.readline

row, column = map(int, input().split())

# 2차원의 형태로 데이터 넣기
data = []
for i in range(row):
    data.append(list(map(int, input().split())))

# 행이 홀수이면, 2차원 배열을 전부 돌면된다 dp 생각안하고 그냥 갑 반환
if row % 2 == 1:
    # row가 3이면 1번, row가 5면 2번, row가 7이면 3번
    print(('R' * (column - 1) + 'D' + 'L' * (column - 1) + 'D')
          * (row // 2) + 'R' * (column - 1))
# 행이 짝수일때
else:
    # 열도 짝수
    if column % 2 == 0:
        # 가장 낮은 기쁨 찾기 limit이 1000이므로
        low = 1000
        # 가장 왼쪽 칸에서 시작
        position = [-1, -1]

        # 피할 원 하나가 홀수 행에 있는지 짝수 행에 있는지 체크
        for i in range(row):
            if i % 2 == 0:
                for j in range(1, column, 2):
                    if low > data[i][j]:
                        low = data[i][j]
                        position = [i, j]
            else:
                for j in range(0, column, 2):
                    if low > data[i][j]:
                        low = data[i][j]
                        position = [i, j]

        # 제외할칸을 기준으로 먼저 이동하기 ( 제외할칸은 position[1] // 2 )
        res = ('D' * (row - 1) + 'R' + 'U' *
               (row - 1) + 'R') * (position[1] // 2)
        x = 2 * (position[1] // 2)
        y = 0
        xbound = 2 * (position[1] // 2) + 1

        while x != xbound or y != row - 1:
            if x < xbound and [y, xbound] != position:
                x += 1
                res += 'R'
            elif x == xbound and [y, xbound - 1] != position:
                x -= 1
                res += 'L'
            if y != row - 1:
                y += 1
                res += 'D'

        res += ('R' + 'U' * (row - 1) + 'R' + 'D' * (row - 1)) * \
            ((column - position[1] - 1) // 2)
        # ((column - position[1] - 1) // 2)는 이동해야하는 나머지 칸 // 2 한 값
        print(res)
    # 열은 홀수
    else:
        print(('D' * (row - 1) + 'R' + 'U' * (row - 1) + 'R')
              * (column // 2) + 'D' * (row - 1))
