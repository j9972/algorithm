import sys

n,m = map(int,input().split())
lines = []
for i in range(m):
    a,b = map(int,input().split())
    lines.append((b,a-1))

lines.sort()
min_val = m

ans = []

def possible():
    num1 = [ i for i in range(n) ]
    num2 = [ i for i in range(n) ]

    for _ , idx in lines:
        num1[idx],num1[idx+1] = num1[idx+1],num1[idx]
    for _ , idx in ans:
        num2[idx],num2[idx+1] = num2[idx+1],num2[idx]

    for i in range(n):
        if num1[i] != num2[i]:
            return False
    
    return True

def choose(cnt):
    global min_val

    if cnt == m:
        if possible():
            min_val = min(min_val, len(ans))
        return

    ans.append(lines[cnt])
    choose(cnt+1)
    ans.pop()
    choose(cnt+1)

choose(0)
print(min_val)