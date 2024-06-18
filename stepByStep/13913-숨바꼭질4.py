from collections import deque

n,k = map(int,input().split())

time = [0] * 100001
node = [0] * 100001

def Print(now):
    arr = []
    tmp = now

    for _ in range(time[now] + 1):
        arr.append(tmp)
        tmp = node[tmp]
    print(' '.join(map(str, arr[::-1])))

def bfs():
    q = deque()
    q.append(n)

    while q:
        now = q.popleft()

        if now == k:
            print(time[now])
            Print(now)
            return now
    
        for i in (now+1, now-1, now*2):
            if 0<=i<=100000 and time[i] == 0:
                time[i] = time[now] + 1
                node[i] = now
                q.append(i)

bfs()