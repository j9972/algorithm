import sys

n = int(input())
string = input()

ans = sys.maxsize
for i in range(1,n+1):
    flag = True
    for idx in range(n-i+1):
        if string[idx:idx+i] in string[idx+1:]:
            flag = False
            break
    if flag:
        ans = min(ans,i)
print(ans)
