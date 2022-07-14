import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
newB_list = []

res = 0

a_list.sort()

for i in range(len(b_list)):
    newB_list.append(b_list[i])

newB_list.sort(reverse=True)

for i in range(n):
    res += a_list[i] * newB_list[i]

print(res)
