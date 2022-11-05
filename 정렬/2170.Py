import sys
input = sys.stdin.readline

n = int(input())

line = []
for i in range(n):
    # x y 지표로 리스형식으로 들어감 -> 2차원 배열
    line.append(list(map(int, input().split())))

line.sort()
total = 0

end = line[0][1]
start = line[0][0]

for i in range(1, n):
    if end >= line[i][1]:
        continue
    elif line[i][0] <= end < line[i][1]:
        end = line[i][1]
    elif end < line[i][0]:
        total += end - start
        end = line[i][1]
        start = line[i][0]

total += end - start
print(total)
