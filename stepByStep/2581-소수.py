m = int(input())
n = int(input())

def prime(cnt):
    if cnt == 1:
        return False
    for i in range(2,cnt//2 +1):
        if cnt % i == 0:
            return False
    return True

arr = []
for i in range(m,n+1):
    if prime(i):
        arr.append(i)

print(sum(arr))
print(arr[0])