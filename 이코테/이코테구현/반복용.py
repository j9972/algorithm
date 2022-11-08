# 문자열 재정렬
import sys
input = sys.stdin.readline

n = input()
str_list = []

num = 0

for i in n:
    if i.isdigit():
        num += int(i)
    else:
        str_list.append(i)

str_list.sort()
str_list.append(num)
res = ''.join(str(s) for s in str_list)
print(res)
