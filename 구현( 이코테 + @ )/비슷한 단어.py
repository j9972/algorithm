# 2607 실버3
import sys
input = sys.stdin.readline

n = int(input())

ans = 0

word = list(input().rstrip())

for _ in range(n-1):
    compare = word[:]
    words = input().rstrip()
    cnt = 0

    for w in words:
        if w in compare:
            compare.remove(w)
        else:
            cnt += 1
    
    if cnt < 2 and len(compare) < 2:
        ans += 1

print(ans)


            
