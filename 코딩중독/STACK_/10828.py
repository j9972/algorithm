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
            d.append(v)
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
        elif order == 'top':
            if len(d) == 0:
                print(-1)
            else:
                print(d[-1])
