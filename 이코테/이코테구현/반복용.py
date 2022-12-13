# 재정렬
import sys
input = sys.stdin.readline

s = input().rstrip()

cnt = 0
ans = []
for i in range(len(s)):
    if s[i].isalpha():
        ans.append(s[i])
    else:
        cnt += int(s[i])
ans.sort()
ans.append(str(cnt))

print(''.join(ans))
