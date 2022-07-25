n = int(input())

time = []
for _ in range(n):
    s, e = map(int, input().split())
    time.append([s, e])

# 시작 시간 -> 끝시간 순차적으로 오름차순을 해준다. ( 끝시간이 같아도 시작시간으로 오름차순이 된다 )
time = sorted(time, key=lambda a: a[0])
time = sorted(time, key=lambda a: a[1])

lastMeeting = 0
count = 0

for i, j in time:
    if i >= lastMeeting:
        count += 1
        lastMeeting = j

print(count)
