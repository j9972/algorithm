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
