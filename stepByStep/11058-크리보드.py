n = int(input())

d = [i for i in range(n+1)]

for i in range(6,n+1):
    d[i] = max(d[i-3] * 2, d[i-4] * 3, d[i-5] * 4)
    
print(d[n])