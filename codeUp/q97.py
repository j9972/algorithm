if __name__ == "__main__":
    arrData = [list(map(int, input().split())) for _ in range(10)]

    x, y = 1, 1

    while True:
        # 먹이를 만나면 멈추기
        if arrData[y][x] == 2:
            arrData[y][x] = 9
            break

        if arrData[y][x] == 0:
            arrData[y][x] = 9
            if arrData[y][x+1] != 1:
                arrData[y][x] = arrData[y][x+1]
                arrData[y][x] = 9
                x += 1
            else:
                if arrData[y+1][x] != 1:
                    arrData[y][x] = arrData[y+1][x]
                    arrData[y][x] = 9
                    y += 1
                else:
                    break

    for y in range(10):
        for x in range(10):
            print(arrData[y][x], end=' ')
        print()
