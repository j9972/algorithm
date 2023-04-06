import sys
input = sys.stdin.readline

data = []
for i in range(int(input())):
    name, kor, eng, math = input().split()
    data.append([name, int(kor), int(eng), int(math)])

data.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))

for d in data:
    print(d[0])