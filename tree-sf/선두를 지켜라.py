n,m = map(int,input().split())

a_, b_ = [], []

def setting(n, a):
    cur = 0
    for _ in range(n):
        v, t = map(int, input().split())
        for i in range(t):
            cur += v
            a.append(cur)
    
    return a

a = setting(n,a_)
b = setting(m,b_)

cnt, leader = 0,0

for i in range(len(a)):
    # 2일떄 a가 앞섬
    if a[i] > b[i]:
        if leader == 1:
            cnt += 1
        leader = 2
    elif a[i] < b[i]:
        if leader == 2:
            cnt += 1
        leader = 1
print(cnt)