# row = 행, col = 열 
# 1번째 방법
# def solution(rows, columns, queries):

#     board = [[0]*(columns+1) for _ in range(rows+1)]
#     ans = []
    
#     cnt = 1
#     for i in range(1,rows+1):
#         for j in range(1,columns+1):
#             board[i][j] = cnt
#             cnt += 1

#     for x1, y1, x2, y2 in queries:
#         tmp = board[x1][y1]
#         mini = tmp
        
#         # 왼쪽 세로
#         for k in range(x1,x2):
#             test = board[k+1][y1]
#             board[k][y1] = test
#             mini = min(mini, test)

#         # 아래쪽 가로
#         for k in range(y1,y2):
#             test = board[x2][k+1]
#             board[x2][k] = test
#             mini = min(mini, test)

#         # 오른쪽 세로
#         for k in range(x2,x1,-1):
#             test = board[k-1][y2]
#             board[k][y2] = test
#             mini = min(mini, test)

#         # 위쪽 가로
#         for k in range(y2,y1,-1):
#             test = board[x1][k-1]
#             board[x1][k] = test
#             mini = min(mini, test)

#         board[x1][y1+1] = tmp
#         #print(board)
#         ans.append(mini)
#     #print(ans)
#     return ans

# 2번째 방법
from collections import deque
def solution(rows, columns, queries):
    ans = deque()
    res = []

    board = [[0]*(columns+1) for _ in range(rows+1)]

    cnt = 1
    for i in range(1,rows+1):
        for j in range(1,columns+1):
            board[i][j] = cnt
            cnt += 1
    
    for x1, y1, x2, y2 in queries:
        for x in range(y2-y1):
            ans.append(board[x1][x2+x])
        for y in range(x2-x1):
            ans.append(board[x1+y][y2])
        for z in range(y2-y1):
            ans.append(board[x2][y2-z])
        for k in range(x2-x1):
            ans.append(board[x2-k][y1])
        
        ans.rotate(1)
        res.append(min(ans))

        for x in range(y2-y1):
            board[x1][y1+x] = ans[0]
            ans.popleft()
        for y in range(x2-x1):
            board[x1+y][y2] = ans[0]
            ans.popleft()
        for z in range(y2-y1):
            board[x2][y2-z] = ans[0]
            ans.popleft()
        for k in range(x2-x1):  
            board[x2-k][y1] = ans[0]
            ans.popleft()  
    print(res)
    return res

solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]])