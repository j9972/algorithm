#실버3 - 2607
import sys
input = sys.stdin.readline

n = int(input())
words = list(input()) # 첫단어
ans = 0

for _ in range(n-1):
    target = words[:]
    word = input()
    cnt = 0

    for w in word:
        if w in target:
            target.remove(w)
        else:
            cnt += 1
    
    if cnt < 2 and len(target) < 2: # len(target) < 2 이유는 변경이 가능하기에
        ans += 1
print(ans)