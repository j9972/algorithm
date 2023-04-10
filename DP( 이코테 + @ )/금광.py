import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n,m = map(int,input().split())

    data = list(map(int,input().split()))

    idx = 0
    d = []
    for i in range(n):
        d.append(data[idx:idx+m])
        idx += m

    for j in range(1,m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = d[i-1][j-1]

            if i == n-1:
                left_down = 0
            else:
                left_down = d[i+1][j-1]
            
            left = d[i][j-1]
            d[i][j] += max(left_up, left_down, left)
    
    res = 0
    for i in range(n):
        res = max(res,d[i][m-1])

    # res = 0
    # for i in d:
    #     res = max(res, max(i))
    
    print(res)