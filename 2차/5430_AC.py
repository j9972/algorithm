import sys
input = sys.stdin.readline
from collections import deque

# R -> 뒤집기
# D -> 첫번째 버리기, 비어있으면 에러

for _ in range(int(input())):

    reversed_flag, flag = False, False

    data = input().rstrip()
    n = int(input())
    arr = input().rstrip()[1:-1]  

    if n == 0 or len(arr) == 0:
        new_arr = deque()
    else:
        new_arr = deque(map(int, arr.split(',')))
    
    for i in data:
        if i == 'R':
            reversed_flag = not reversed_flag
        else:
            if len(new_arr) == 0:
                flag = True
                break

            if reversed_flag:
                new_arr.pop()
            else:
                new_arr.popleft()
        
    if flag:
        print('error')
    else:
        #print(new_arr)

        if reversed_flag:
            print('[' + ','.join(map(str, reversed(new_arr))) + ']')
        else:
            print('[' + ','.join(map(str, new_arr)) + ']')