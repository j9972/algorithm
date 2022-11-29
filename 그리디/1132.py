import sys
input = sys.stdin.readline

n = int(input())
str1 = input()
str2 = input()

str1 = str1[:-1]
str2 = str2[:-1]

list_1 = []
for i in range(len(str1)):
    m = 10**(len(str1) - (i+1))
    print(m)
    if m == 0:
        m = 1
    list_1.append(str(m)+str1[i])

list_2 = []
for i in range(len(str2)):
    m = 10**(len(str2) - (i+1))
    print(m)
    if m == 0:
        m = 1
    list_2.append(str(m)+str2[i])

for i in list_1:
    for j in list_2:
