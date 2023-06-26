# Lv2 - DP 
def solution(board):
    ans = 0
    r = len(board) 
    c = len(board[0])
    d = [[0] * (c+1) for _ in range(r+1)]
    
    for i in range(1,r+1):
        for j in range(1,c+1):
            if board[i-1][j-1] == 1:
                d[i][j] = min(d[i][j-1], d[i-1][j], d[i-1][j-1]) + 1
            
            ans = max(ans, d[i][j])

    return ans ** 2