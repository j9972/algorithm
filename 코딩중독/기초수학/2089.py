N = int(input())
ans = ''
if N == 0:
    print(0)
    exit()

while N != 0:
    if N % -2:
        N = N//-2+1
        ans = '1'+ans
    else:
        N //= -2
        ans = '0'+ans

print(int(ans))
