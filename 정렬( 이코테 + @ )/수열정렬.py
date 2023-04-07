import sys
input = sys.stdin.readline

# p 수열 = A 수열위 각 숫자가 몇번쨰로 작은지 0부터 정리 해준 수열

n = int(input())
a = list(map(int,input().split()))
sorted_a = sorted(a)

p = [0 for _ in range(n)]

for i in range(n):
    idx = sorted_a.index(a[i])
    p[i] = idx
    sorted_a[idx] -= 1
    
print(*p)

