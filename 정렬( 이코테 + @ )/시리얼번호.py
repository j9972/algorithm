import sys
input = sys.stdin.readline

serial_num = []
for i in range(int(input())):
    serial_num.append(input().rstrip())

def count(str):
    tot = 0
    for i in str:
        if i.isdigit():
            tot += int(i)
    return tot

serial_num.sort(key=lambda x:(len(x),count(x),x))


for s in serial_num:
    print(s)