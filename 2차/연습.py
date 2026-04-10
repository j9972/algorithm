import sys
input = sys.stdin.readline

from collections import deque

for _ in range(int(input())):

    char = input().rstrip()
    n = int(input())
    temp = input().rstrip()[1:-1]

    if n == 0 or len(temp) == 0:
        q = deque()
    else:
        q = deque(map(str,temp.split(',')))

    flag, reversed_flag = False, False

    for i in char:
        if i == 'R':
            reversed_flag = not reversed_flag
        else:
            if len(q) == 0:
                flag = True
                break
            else:
                if not reversed_flag:
                    q.popleft()
                else:
                    q.pop()
    
    if flag:
        print('error')
    else:
        if reversed_flag:
            print('[' + ','.join(reversed(q)) + ']')
        else:
            print('[' + ','.join(q) + ']')

