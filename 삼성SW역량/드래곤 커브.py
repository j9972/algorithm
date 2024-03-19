import sys

n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

temp = [
    [0 for _ in range(101)]
    for _ in range(101)
]

dxs,dys = [0,-1,0,1], [1,0,-1,0]

for i in arr:
    start_y, start_x, d, g = i

    temp_list = [(start_x, start_y)]
    temp_list.append((start_x + dxs[d], start_y + dys[d]))

    for _ in range(g):
        end_x, end_y = temp_list[-1]

        for j in range(len(temp_list)-2, -1, -1):
            cur_x,cur_y = temp_list[j]

            temp_list.append((end_x - (end_y - cur_y), end_y + (end_x - cur_x)))

    for i,j in temp_list:
        temp[i][j] = 1

ans = 0
for i in range(100):
    for j in range(100):
        if temp[i][j] == temp[i+1][j] == temp[i][j+1] == temp[i+1][j+1] == 1:
            ans += 1
print(ans)