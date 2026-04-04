import sys
input = sys.stdin.readline

n = int(input())
values = list(map(int,input().split()))

dic = {}

set_values = sorted(set(values))

for i, val in enumerate(set_values):
    #print("i : {}, val : {}".format(i, val))
    dic[val] = i

for i in values:
    print(dic[i], end=' ')
print()
