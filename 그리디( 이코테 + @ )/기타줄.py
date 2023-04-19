import sys
input = sys.stdin.readline

n,m = map(int,input().split())

guitar = []
for i in range(m):
    guitar.append(list(map(int,input().split())))

guitar.sort(key=lambda x:(x[0],x[1]))
print(guitar)