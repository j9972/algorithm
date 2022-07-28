# 모든 자릿수의 합이 3의 배수가 되면 된다.1

n = input()

n = sorted(n, reverse=True)

ans = 0

if '0' not in n:
    print(-1)
else:
    for i in n:
        ans += int(i)
    if ans % 3 != 0:
        print(-1)
    else:
        print(''.join(n))
