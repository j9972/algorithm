from collections import deque

n = int(input())

q = deque()
q.append((n,0))

visited = set()
visited.add(n)

ans = 0
def bfs():
    global ans
    while q:
        val, res = q.popleft()

        if val == 1:
            ans = res
            break 
            
        if val // 3 not in visited and val % 3 == 0:
            visited.add(val //3)
            q.append((val //3, res+1))

        if val // 2 not in visited and val % 2 == 0:
            visited.add(val //2)
            q.append((val //2, res+1))

        if val -1 not in visited:
            visited.add(val -1)
            q.append((val -1, res+1))

        if val +1 not in visited:
            visited.add(val +1)
            q.append((val +1, res+1))
        
bfs()
print(ans)

