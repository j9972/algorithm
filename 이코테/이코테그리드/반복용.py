# 모험가 길드
#import sys
#input = sys.stdin.readline

# n = int(input())

# data = list(map(int, input().split()))
# data.sort()

# while True:

#  곱하기 혹은 더하기
s = input()
ans = int(s[0])

for i in range(1, len(s)):
    if ans <= 1 or int(s[i]) <= 1:
        ans += int(s[i])
    else:
        ans *= int(s[i])

print(ans)
