# 프린터 큐
import sys
input = sys.stdin.readline


for _ in range(int(input())):
    # 개수, 뽑고 싶은 유인물 위치
    n, m = map(int, input().split())
    count = 0
    q = list(map(int, input().split()))

    while True:
        target = q[m]

        if m == -1:
            m = len(q) - 1

        if q[0] < max(q):
            q.append(q[0])
            q.pop(0)
            m -= 1
        else:
            count += 1
            if q[0] == target and m == 0:
                print(count)
                break
            else:
                q.pop(0)
                m -= 1
