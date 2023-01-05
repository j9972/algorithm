import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()

t = 1
for i in data:  # 한번 돌때마다 전부 돌리면서 안되는게 있는지 여부 체크를 해서 하는것 ( 하나하나가 아니라 전부 체크 )
    if t < i:
        break
    t += i

print(t)
