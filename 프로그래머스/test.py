from collections import deque
def solution(rows, cols, queries):
    ans = []
    cnt = 1
    board = [[0]*(cols+1) for _ in range(rows+1)]
    for i in range(1,rows+1):
        for j in range(1,cols+1):
            board[i][j] = cnt
            cnt += 1
    
    for x1,y1,x2,y2 in queries:
        tmp = board[x1][y1]
        mini = tmp 
        
        for k in range(x1,x2):
            test = board[k+1][y1]
            board[k][y1] = test
            mini = min(mini, test)

        for k in range(y1,y2):
            test = board[x2][k+1]
            board[x2][k] = test
            mini = min(mini, test)

        for k in range(x2,x1,-1):
            test = board[k-1][y2]
            board[k][y2] = test
            mini = min(mini, test)

        for k in range(y2,y1,-1):
            test = board[x1][k-1]
            board[x1][k] = test
            mini = min(mini, test)

        board[x1][y1+1] = tmp
        ans.append(mini)
    print(ans)   
    return ans
solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]])