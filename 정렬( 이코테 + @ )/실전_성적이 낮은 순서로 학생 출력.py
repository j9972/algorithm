import sys
input = sys.stdin.readline

data = []
for i in range(int(input())):
    name, grade = input().split()
    data.append([name,int(grade)])

data = sorted(data, key=lambda x: x[1])

for i in data:
    print(i[0], end = ' ')