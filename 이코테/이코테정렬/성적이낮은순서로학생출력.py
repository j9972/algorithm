n = int(input())

board = []
for i in range(n):
    data = input().split()
    board.append((data[0], int(data[1])))

board.sort(key=lambda student: student[1])

for student in board:
    print(student[0], end=' ')
