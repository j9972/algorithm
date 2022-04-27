import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    d = []

    for _ in range(n):
        word = input().split()
        order = word[0]

        if order == 'push':
            v = word[1]
            d.insert(0, v)
        elif order == 'pop':
            if len(d) == 0:
                print(-1)
            else:
                print(d.pop())
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
                print(d[len(d) - 1])
        elif order == 'back':
            if len(d) == 0:
                print(-1)
            else:
                print(d[0])
