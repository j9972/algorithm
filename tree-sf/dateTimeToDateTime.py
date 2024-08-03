a,b,c = map(int,input().split())

ans = 0

if a < 11:
    ans = -1
elif a == 11 and b < 11:
    ans = -1
elif a == 1 and b == 11 and c < 11:
    ans = -1
else:
    while True:
        if a == 11 and b == 11 and c == 11:
            break
        
        c -= 1
        ans += 1

        if c < 0:
            c = 59
            b -= 1

            if b < 0:
                b = 23
                c = 59
                a -= 1


print(ans)


# 2번 방법
ans = (a*24+b*60+c*60) - (11*24 + 11*60 + 11*60)

if ans < 0:
    print(-1)
else:
    print(ans)
