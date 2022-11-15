import sys
input = sys.stdin.readline

name = input()

res = 0

mini = len(name) - 1

for i, char in enumerate(name):
    res += min(ord('Z')-ord(char)+1, ord(char)-ord('A'))

    next = i + 1
    while next < len(name) and name[next] == 'A':
        next += 1

    # 기존, A같은거 여러개 왼쪽부터, A같은거 여러개 오른쪽부터
    mini = min(mini, i*2+len(name) - next, i+2*(len(name) - next))

res += mini

print(res)
