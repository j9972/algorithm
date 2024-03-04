k,n = map(int,input().split())

ans = list()

def Print():
    for i in ans:
        print(i,end=' ')
    print()

def choose(idx):
 
    if idx == n:
        Print()
        return

    for i in range(1,k+1):
        if idx >= 2 and (ans[-1] == ans[-2] == i):
            continue
        ans.append(i)
        choose(idx+1)
        ans.pop()
choose(0)
