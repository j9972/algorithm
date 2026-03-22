import sys
input = sys.stdin.readline

dic = {}
n_list = []
n = int(input())

for i in range(n):
    val = int(input())

    n_list.append(val)

    if val in dic:
        dic[val] += 1
    else:
        dic[val] = 1

print(round(sum(n_list)/n))
print(sorted(n_list)[n//2])

mean = -10e9
if n == 1:
    mean = n_list[0]
else:
    if sorted(dic.items(), key=lambda x : (-x[1], x[0]))[0][1] == sorted(dic.items(), key=lambda x : (-x[1], x[0]))[1][1]:
        mean = sorted(dic.items(), key=lambda x : (-x[1], x[0]))[1][0]
    else:
        mean = sorted(dic.items(), key=lambda x : (-x[1], x[0]))[0][0]

print(mean)

print(abs(max(n_list) - min(n_list)))