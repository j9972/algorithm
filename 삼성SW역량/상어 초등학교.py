import sys

n = int(input())

dxs, dys = [-1,0,0,1], [0,-1,1,0]

# 학생번호, 좋아하는 친구 4명
arr = [
    list(map(int,input().split()))
    for _ in range(n*n)
]

temp = [
    [0 for _ in range(n)]
    for _ in range(n)
]

ans = 0
score = {
    0 : 0,
    1 : 1,
    2 : 10,
    3 : 100,
    4 : 1000
}

def in_range(x,y):
    return 0<=x<n and 0<=y<n

# 북 서 동 남 순서로 ( 행-열 순서 맞춤 )
def how_many_friends_i_like(x,y,friends):
    like_cnt, empty_cnt = 0, 0
    for dx,dy in zip(dxs,dys):
        nx,ny = x + dx, y + dy

        if not in_range(nx,ny):
            continue

        if temp[nx][ny] in friends:
            like_cnt += 1
        
        if temp[nx][ny] == 0:
            empty_cnt += 1
    
    return like_cnt, empty_cnt



for i in arr:
    cur_num, f1,f2,f3,f4 = i

    tmp = [f1,f2,f3,f4]

    max_like_cnt, max_empty_cnt, cur_x, cur_y = 0,0,-1,-1
    
    for x in range(n):
        for y in range(n):
            if temp[x][y] != 0:
                continue

            like_cnt, empty_cnt = how_many_friends_i_like(x,y,tmp)
            
            if max_like_cnt < like_cnt:
                max_like_cnt = like_cnt
                max_empty_cnt = empty_cnt
                cur_x,cur_y = x,y
                

            elif max_like_cnt == like_cnt:
                
                if max_empty_cnt < empty_cnt:
                    
                    max_empty_cnt = empty_cnt
                    cur_x,cur_y = x,y
                
                elif max_empty_cnt == empty_cnt:
                    if cur_x == -1 and cur_y == -1:
                        cur_x,cur_y = x,y
                    elif cur_x > x:
                        cur_x,cur_y = x,y
                    elif cur_x == x and cur_y > y:
                        cur_x,cur_y = x,y


            
    
    temp[cur_x][cur_y] = cur_num

for x in range(n):
    for y in range(n):
        for i in arr:
            cur_num, f1,f2,f3,f4 = i

            tmp = [f1,f2,f3,f4]

            cnt = 0

            if temp[x][y] == cur_num:

                for dx,dy in zip(dxs, dys):
                    nx,ny = x + dx, y + dy

                    if not in_range(nx,ny):
                        continue

                    if temp[nx][ny] in tmp:
                        cnt += 1
            
            ans += score[cnt]
print(ans)
