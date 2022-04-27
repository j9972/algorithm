from collections import deque
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    d = deque()

    for _ in range(n):
        word = input().split()
        order = word[0]

        if order == 'push_front':
            v = word[1]
            d.appendleft(v)
        elif order == 'push_back':
            v = word[1]
            d.append(v)

        elif order == 'pop_front':
            if len(d) == 0:
                print(-1)
            else:
                print(d[0])
                d.popleft()
        elif order == 'pop_back':
            if len(d) == 0:
                print(-1)
            else:
                print(d[len(d) - 1])
                d.pop()

        elif order == 'size':
            print(len(d))
        elif order == 'empty':
            if len(d) == 0:
                print(1)
            else:
                print(0)
        elif order == 'front':
            if len(d) == 0:
                print(-1)
            else:
                print(d[0])
        elif order == 'back':
            if len(d) == 0:
                print(-1)
            else:
                print(d[len(d) - 1])
