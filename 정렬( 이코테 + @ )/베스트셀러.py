import sys
input = sys.stdin.readline

dic = dict()

for i in range(int(input())):
    book = input().rstrip()
    if book not in dic.keys():
        dic[book] = 1
    else:
        dic[book] += 1

dic = sorted(dic.items(), key=lambda x:(-x[1],x[0]))

print(dic[0][0])