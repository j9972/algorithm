import sys
input = sys.stdin.readline

n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i],b[i] = b[i],a[i]
    else: # 이걸 하는 이유는 시간 복잡도를 조금이라도 줄이기 우히마 
        break
print(sum(a))