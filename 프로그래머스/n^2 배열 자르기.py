# 틀림 - 시간 초과
def solution(n, left, right):
    
    board = []
    
    i = 1
    while i != n+1:
        for _ in range(i):
            board.append(i)
        
        for j in range(i+1,n+1):
            board.append(j)
        i += 1
    
    return board[left:right+1]

# 틀림 - 시간 초과
def solution(n, left, right):
    
    board = []
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            board.append(max(i,j))
    
    return board[left:right+1]

def solution(n, left, right):
    board = []
    
    for i in range(left, right+1):
        a = i // n
        b = i % n
        if a < b:
            board.append(b+1)
        else:
            board.append(a+1)
    
    return board


