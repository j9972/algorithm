a_x1, a_y1, a_x2, a_y2 = map(int,input().split())
b_x1, b_y1, b_x2, b_y2 = map(int,input().split())
m_x1, m_y1, m_x2, m_y2 = map(int,input().split())

temp = [
    [0 for _ in range(2001)]
    for _ in range(2001)
]

for x in range(a_x1+1000, a_x2+1000):
    for y in range(a_y1+1000, a_y2+1000):
        temp[x][y] = 1

for x in range(b_x1+1000, b_x2+1000):
    for y in range(b_y1+1000, b_y2+1000):
        temp[x][y] = 1

for x in range(m_x1+1000, m_x2+1000):
    for y in range(m_y1+1000, m_y2+1000):
        temp[x][y] = 0

print(sum(sum(row) for row in temp))


# 2번

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

for i, (x1, y1, x2, y2) in enumerate(arr, start=1):
    x1, y1 = x1 + 100, y1 + 100
    x2, y2 = x2 + 100, y2 + 100
    
    for x in range(x1, x2):
        for y in range(y1, y2):
            temp[x][y] = i

area = 0
for x in range(0, 2001):
    for y in range(0, 2001):
        if temp[x][y] == 1 or temp[x][y] == 2:
            area += 1

print(area)