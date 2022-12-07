import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()

cnt = 0


def process(idx, goodNumber):
    tmp = data[:idx] + data[idx+1:]
    s = 0
    e = n - 2

    while s < e:
        tot = tmp[s] + tmp[e]
        if tot < goodNumber:
            s += 1
        elif tot > goodNumber:
            e -= 1
        else:
            return True
    return False


for i in range(len(data)):
    if process(i, data[i]):
        cnt += 1
print(cnt)
