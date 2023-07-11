def solution(places):
    answer = []
    
    # 맨해튼 거리가 1인경우 상하좌우
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    # 맨해튼 거리가 2인경우가 되는 8가지 경우 -> 2칸 띄워진 상하좌우, 4가지 대각선
    da = [2, -2, 0, 0, 1, 1, -1, -1]
    db = [0, 0, 2, -2, -1, 1, -1, 1]
    
    for p in places:
        flag = 1
        for i in range(5):
            for j in range(5):
                
                if p[i][j] == "P":
                    for k in range(4):
                        next_x = i + dx[k]
                        next_y = j + dy[k]
                        
                        if 0 <= next_x <= 4  and 0 <= next_y <= 4:
                            if p[next_x][next_y] == "P":
                                flag = 0
                                break
                                
                    for k in range(8):
                        next_x = i + da[k]
                        next_y = j + db[k]
                        
                        if 0 <= next_x <= 4  and 0 <= next_y <= 4:
                            if p[next_x][next_y] == "P":
                                if(abs(next_x - i) == 2):
                                    if(p[(next_x + i) // 2][next_y] == "O"):
                                        flag = 0
                                        break
                                elif(abs(next_y - j) == 2):
                                    if(p[next_x][(next_y + j) // 2] == "O"):
                                        flag = 0
                                        break
                                elif(p[next_x][j] == "O" or p[i][next_y] == "O"):
                                        flag = 0
                                        break
                    if flag == False:
                        break
                if flag == False:
                        break
        answer.append(flag)
    return answer