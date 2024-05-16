n = int(input())

arr = list(map(int,input().split()))

def prime(cnt):
    if cnt == 1:
        return False
    for i in range(2,cnt//2+1):
        if cnt % i == 0:
            return False
    return True

cnt = 0
for i in arr:
    if prime(i):
        cnt += 1
print(cnt)