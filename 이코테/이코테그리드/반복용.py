# 문자열 뒤집기

import sys
input = sys.stdin.readline

data = input()


zeroCount = 0
oneCount = 0

data_list = list(data)

if data[0] == '1':
    oneCount += 1
else:
    zeroCount += 1


for i in range(len(data_list)-1):
    if data[i] != data[i+1]:  # i+1 때문에 처음 시작하는 데이터의 값을 알아야 한다.
        if data[i+1] == '1':
            oneCount += 1
        else:
            zeroCount += 1
print(min(zeroCount, oneCount))
