n,m = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

dxs,dys = [-1,1,0,0], [0,0,-1,1]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

values = []


for i in range(n):
    for j in range(n):
        for k in range(n + 1):
            cnt = 0

            visited = [(i,j)]
            st = [(i,j)]

            while st:
                x,y = st.pop(0)

                if arr[x][y] == 1:
                    cnt += 1

                for dx, dy in zip(dxs,dys):
                    nx, ny = x + dx, y + dy
                    
                    if in_range(nx,ny) and abs(nx-i) + abs(ny-j) <= k and (nx,ny) not in visited:
                        visited.append((nx,ny))
                        st.append((nx,ny))

            if cnt * m >= 2 * k * (k + 1) + 1:
                values.append(cnt)


values.sort(reverse=True)

if len(values) == 0:
    print(0)
else:
    print(values[0])


# 2번

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]


# 주어진 k에 대하여 마름모의 넓이를 반환합니다.
def get_area(k):
    return k * k + (k + 1) * (k + 1)


# 주어진 k에 대하여 채굴 가능한 금의 개수를 반환합니다.
def get_num_of_gold(row, col, k):
    return sum([
        grid[i][j]
        for i in range(n)
        for j in range(n)
        if abs(row - i) + abs(col - j) <= k
    ])


max_gold = 0

# 격자의 각 위치가 마름모의 중앙일 때 채굴 가능한 금의 개수를 구합니다.
for row in range(n):
    for col in range(n):
        for k in range(2 * (n - 1) + 1):
            num_of_gold = get_num_of_gold(row, col, k)
            
            # 손해를 보지 않으면서 채굴할 수 있는 최대 금의 개수를 저장합니다.
            if num_of_gold * m >= get_area(k):
                max_gold = max(max_gold, num_of_gold)

print(max_gold)