arr = [
    list(map(int,input()))
    for _ in range(3)
]

line = [
    [arr[0][0],arr[0][1],arr[0][2]],
    [arr[1][0],arr[1][1],arr[1][2]],
    [arr[2][0],arr[2][1],arr[2][2]],

    [arr[0][0],arr[1][0],arr[2][0]],
    [arr[0][1],arr[1][1],arr[2][1]],
    [arr[0][2],arr[1][2],arr[2][2]],

    [arr[0][0],arr[1][1],arr[2][2]],
    [arr[2][0],arr[1][1],arr[0][2]],
]


temp_total = list()
for i in line:
    temp = set()
    for j in i:
        temp.add(j)
    
    if len(temp) == 2:
        if temp not in temp_total:
            temp_total.append(temp)

print(len(temp_total))