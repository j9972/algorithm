n,m = map(int,input().split())

ans = []

def Print():
    for i in ans:
        print(i, end=' ')
    print()

def choose(num, idx):
    if num == n+1:
        if idx == m:
            Print()
        return
    ans.append(num)
    choose(num+1, idx+1)
    ans.pop()
    choose(num+1, idx)
choose(1,0)
