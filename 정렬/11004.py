import sys
input = sys.stdin.readline

n, k = map(int, input().split())

board = list(map(int, input().split()))
board.sort()

# k번째 -> index 로 생각해서 k-1
print(board[k-1])
