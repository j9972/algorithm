import sys
input = sys.stdin.readline

data = input().rstrip()
res =0
l = []
for i in data:
    if i.isdigit():
        res += int(i)
    else:
        l.append(i)

l.sort()
ans = ''
for i in l:
    ans+=i

print(ans+str(res))
