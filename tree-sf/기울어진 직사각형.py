n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

# 1 -> 2 -> 3 -> 4
dxs,dys = [-1,-1,1,1],[1,-1,-1,1]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def check(x,y,k,l): 
    move_cnt=[k,l,k,l]
    cnt=0
    for dx,dy,move_cnt in zip(dxs,dys,move_cnt):
        for itr in range(move_cnt):
            x, y= x + dx, y+ dy

            if not in_range(x,y):
                return 0
            
            cnt+=arr[x][y]
    return cnt

max_cnt = 0
for x in range(n):
    for y in range(n):
        for upper in range(1,n):
            for lower in range(1,n):
                max_cnt = max(max_cnt, check(x,y,upper,lower))
                # move_cnt = [upper, lower, upper, lower]
                # cnt = 0
                # f = True

                # for dx, dy, m_cnt in zip(dxs, dys, move_cnt):
                #     for _ in range(m_cnt):
                #         nx,ny = x + dx, y + dy

                #         if not in_range(nx,ny):
                #             cnt = 0
                #             f = False
                #             break
                        
                #         cnt += arr[nx][ny]
                    
                #     if not f:
                #         break

                # max_cnt = max(max_cnt, cnt)


print(max_cnt)