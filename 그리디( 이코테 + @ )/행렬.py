# 1080 - 실버1
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

a_matrix = []
for i in range(n):
    a_matrix.append(list(map(int,input().rstrip())))

b_matrix = []
for i in range(n):
    b_matrix.append(list(map(int,input().rstrip())))

def overturn(x,y):
    for i in range(x,x+3):
        for j in range(y,y+3):
            if a_matrix[i][j] == 0:
                a_matrix[i][j] = 1
            else:
                a_matrix[i][j] = 0

cnt = 0
# n<3,m<3 인데 a_matrix,b_matrix 가 같으면 cnt는 -1 이 아니니까 a_matrix != b_matrix 조건 필요
if (n < 3 or m < 3) and a_matrix != b_matrix:
    cnt = -1
else:
    for i in range(n-2): # 0 부터 범위 시작이니까 -2가 맞다
        for j in range(m-2):
            if a_matrix[i][j] != b_matrix[i][j]:
                overturn(i,j)
                cnt += 1

if cnt != -1:
    if a_matrix != b_matrix:
        cnt = -1

print(cnt)