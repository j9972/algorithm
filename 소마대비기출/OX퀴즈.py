# 브2 - 8958
import sys
input = sys.stdin.readline


for tc in range(int(input())):
    s = input()
    d = [0] * (len(s)+1)

    if s[0] == 'O':
        d[0] = 1
    else:
        d[0] = 0

    for i in range(1, len(s)+1):
        if s[i-1] == 'O':
            if s[i] == 'O':
                d[i] = d[i-1] + 1
            else:
                d[i] = 0
        else:
            if s[i] == 'O':
                d[i] = 1
            else:
                d[i] = 0
    print(sum(d[len(s)]))
