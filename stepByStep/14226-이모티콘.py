from collections import deque

s = int(input())

d = [[0] * (1001) for _ in range(1001)]
d[1][0] = True

q = deque()
q.append([1,0,0]) # 화면, 클립, 연산수

def in_range(monitor, clip):
    return 0<=monitor<1001 and 0<=clip<1001

while q:
    monitor, clip, cnt = q.popleft()

    if monitor == s:
        print(cnt)
        break
    
    for i in range(3):
        if i == 0:
            new_monitor , new_clip = monitor, monitor
        elif i == 1:
            new_monitor , new_clip = clip + monitor, clip
        else:
            new_monitor , new_clip = monitor - 1, clip
        
        if not in_range(new_monitor,new_clip) or d[new_monitor][new_clip] == 1:
            continue

        d[new_monitor][new_clip] = 1
        q.append([new_monitor, new_clip, cnt + 1])
        


