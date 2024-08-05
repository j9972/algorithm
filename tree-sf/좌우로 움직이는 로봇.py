n,m = map(int,input().split())

a = [
    list(input().split())
    for _ in range(n)
]

b = [
    list(input().split())
    for _ in range(m)
]

ans = 0

A = [0] * 1000001
B = [0] * 1000001

a_idx = 1
for t, d in a:
    for _ in range(int(t)):
        A[a_idx] = A[a_idx - 1] + (1 if d == 'R' else -1)
        a_idx += 1

b_idx = 1
for t, d in b:
    for _ in range(int(t)):
        B[b_idx] = B[b_idx - 1] + (1 if d == 'R' else -1)
        b_idx += 1

if a_idx < b_idx:
    for i in range(a_idx,b_idx):
        A[i] = A[i-1]
elif a_idx > b_idx:
    for i in range(b_idx,a_idx):
        B[i] = B[i-1]

for i in range(1,max(a_idx, b_idx)):
    if A[i-1] != B[i-1] and A[i] == B[i]:
        ans += 1
print(ans)