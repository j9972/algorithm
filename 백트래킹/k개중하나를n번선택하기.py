k,n = map(int,input().split())

ans = list()

def Print():
    for i in ans:
        print(i,end=' ')
    print()

def choose(cnt):

    if cnt == n:
        Print()
        return
    
    for i in range(1,k+1):
        ans.append(i)
        choose(cnt + 1)
        ans.pop()
choose(0)