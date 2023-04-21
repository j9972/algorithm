import sys
input = sys.stdin.readline

n = input().rstrip()
l,r= 0,0
length = len(n) 
for i in range(length):
    if i < length//2:
        l += int(n[i])
    else:
        r += int(n[i])

if l == r:
    print("LUCKY")
else:
    print("READY")

