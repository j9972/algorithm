chulsoo = [list(map(int, input().split())) for _ in range(5)]
MC = [list(map(int, input().split())) for _ in range(5)]

count = 0  # 사회자가 숫자를 부른 횟수를 세는 변수


# 빙고 개수 세기
def solution(array: list):
    bingo_number = 0
    # 가로가 빙고일때
    for i in range(5):
        if sum(array[i]) == 0:
            bingo_number += 1

    # 세로가 빙고일때
    for i in range(5):
        count_temp = 0
        for j in range(5):
            if array[j][i] == 0:
                count_temp += 1
        if count_temp == 5:
            bingo_number += 1

    # 대각선이 빙고일 때
    temp_up = []  # 우하단 빙고
    temp_down = []  # 우상단 빙고
    for i in range(5):
        temp_up.append(array[i][i])
        temp_down.append(array[i][4 - i])

    if sum(temp_up) == 0:
        bingo_number += 1
    if sum(temp_down) == 0:
        bingo_number += 1

    return bingo_number


for i in range(5):
    for j in range(5):
        for k in range(5):
            for h in range(5):  # 사회자가 부른 수를 비교하기위해 4번의 반복문을 돈다.
                if MC[i][j] == chulsoo[k][h]:  # 만약 해당 번호를 찾았다면
                    chulsoo[k][h] = 0  # 그 번호를 0으로 만들고
                    count += 1  # 부른횟수를 +1 해준다.
                if count >= 12:  # 만약 count 값이 12이상이라면(3빙고가 나오기 위한 최소한의 조건)
                    if solution(chulsoo) >= 3:  # 빙고개수를 세어 3이상이라면
                        print(count)  # 그 횟수를 출력하고
                        exit()  # 코드종료한다.