s = int(input())

cnt = 0

while s >= cnt:
    s -= cnt
    cnt += 1
    print("s: {}, cnt : {}".format(s, cnt))

print(cnt-1)