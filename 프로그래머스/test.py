def solution(n):
    board = [[0] * i for i in range(1, n+1)]
    
    x,y = -1,0 # x는 처음에 아래 방향으로 움직이니까 -1
    cnt = 1

    for i in range(n):
        for _ in range(i,n):
            if i % 3 == 0: # 아래 방향
                x += 1
            elif i % 3 == 1: # 오른쪽
                y += 1
            elif i % 3 == 2: # 왼쪽 대각
                y -= 1
                x -= 1
            
            board[x][y] = cnt
            cnt += 1
    print(board)
    print(sum(board,[]))
    return sum(board,[])
solution(3)

#test