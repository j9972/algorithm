import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
add, minus, multi, div = map(int, input().split())

maxvalue = -int(10e9)
minvalue = int(10e9)


def dfs(i, now):
    # 연산자 개수, 현재값 순서로 parameter 받기
    global add, minus, multi, div, maxvalue, minvalue
    if i == n:
        maxvalue = max(now, maxvalue)
        minvalue = min(now, minvalue)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, data[i] + now)
            add += 1
        elif minus > 0:
            minus -= 1
            dfs(i+1, now - data[i])
            minus += 1
        elif multi > 0:
            multi -= 1
            dfs(i+1, data[i] * now)
            multi += 1
        elif div > 0:
            div -= 1
            dfs(i+1, int(now / data[i]))
            div += 1


dfs(1, data[0])
print(maxvalue)
print(minvalue)
