# 실버 3 - 20310
import sys
input = sys.stdin.readline

s = list(input().rstrip())
zero = s.count('0')//2
one = s.count('1')//2

# 1은 앞에서부터, 0은 뒤에서부터 지워주면 된다.
for _ in range(zero):
    s.pop(-s[::-1].index('0') -1 )
    print(s)
for _ in range(one):
    s.pop(s.index('1'))
#print(''.join(s))
