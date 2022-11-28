import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())  # 보석 개수 , 가방 개수

jewel = []
for i in range(n):
    m, v = map(int, input().split())
    jewel.append([m, v])

weight = []
for i in range(k):
    weight.append(int(input()))

weight.sort()

idx = 0
for i in range(len(jewel)):
    if jewel[i][1] > max(weight):
        idx = i
        break

jewel = jewel[:idx]

jewel.sort(key=lambda x: x[0])
print(jewel)

q = []
for i in range(len(weight)):
    if jewel[i][0] <= weight[i]:
        q.append(jewel[i][1])

print(sum(q))
