import sys
input = sys.stdin.readline

n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

crane.sort(reverse=True)
box.sort(reverse=True)


cnt = 0

if box[0] > crane[0]:
    print(-1)
    sys.exit(0)
else:
    time = 0
    while box:
        if not box:
            break
        for c in crane:
            for b in box:
                if c >= b:
                    box.remove(b)
                    break
        time += 1
    print(time)
