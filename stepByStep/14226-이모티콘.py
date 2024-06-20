from collections import deque

s = int(input())

q = deque()
q.append([1,0,0]) # 화면, clip, cnt

d = [
    [0] * (1001)
    for _ in range(1001)
]

d[1][0] = 1

def in_range(a,b):
    return 0<=a<1001 and 0<=b<1001

while q:
    monitor, clip, cnt = q.popleft()

    if monitor == s:
        print(cnt)
        break

    for i in range(3):
        if i == 0:
            new_monitor, new_clip = monitor, monitor
        elif i == 1:
            new_monitor, new_clip = monitor + clip, clip
        else:
            new_monitor, new_clip = monitor - 1, clip
        
        if not in_range(new_monitor,new_clip) or d[new_monitor][new_clip] == 1:
            continue

        d[new_monitor][new_clip] = 1
        q.append([new_monitor,new_clip,cnt+1])
