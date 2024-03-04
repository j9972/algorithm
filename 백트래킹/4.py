n = int(input())

visited = [False] * (n+1)

ans = list()

def Print():
    for i in ans:
        print(i,end=' ')
    print()

def choose(idx):
    if idx == n:
        Print()
        return
    
    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = True
            ans.append(i)

            choose(idx+1)

            ans.pop()
            visited[i] = False

choose(0)
