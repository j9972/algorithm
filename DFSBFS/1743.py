# # dfs -> 음식물 피하기
# # recurisonError 뜨면 아래 2줄 추가해주기
# import sys
# sys.setrecursionlimit(10**9)
# n, m, k = map(int, input().split())

# board = [[0]*(m+1) for _ in range(n+1)]
# for i in range(k):
#     r, c = map(int, input().split())
#     board[r][c] = 1

# visited = [[False]*(m+1) for _ in range(n+1)]

# num = 0
# count = []


# def dfs(x, y):
#     global num
#     if 1 <= x < n+1 and 1 <= y < m+1 and board[x][y] == 1 and not visited[x][y]:
#         visited[x][y] = True
#         num += 1
#         board[x][y] = 0
#         dfs(x-1, y)
#         dfs(x+1, y)
#         dfs(x, y-1)
#         dfs(x, y+1)
#         return True
#     return False


# for i in range(1, n+1):
#     for j in range(1, m+1):
#         if dfs(i, j) == True:
#             count.append(num)
#             num = 0

# print(max(count))


person = input("생일인 사람의 이름을 입력하시오: ")

def song(person="kim"):
    print("Happy Birthday to you!\n")
    print("Happy Birthday to you!\n")
    print(f"Happy Birthday to dear {person}")
    print("Happy Birthday to you!")

song(person)
