# 여기서 진짜 중요한 점은 2가지 이상의 브랜드를 섞어서 기타줄을 살수 있다는 점이다
# 또 다른 좀은 6개까지 패키지를 샀을때 n 보다 커도 최솟값이면 상관없다 ( 3번째 예제 )

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int, input().split())

pack = []
single = []

# 브랜드의 개수 만큼 for문을 돌려서 리스트 박스에 넣어준다
for i in range(m):
    p, s = map(int, input().split())
    pack.append(p)
    single.append(s)

mPack = min(pack)

res = 0
while n > 0:
    if n >= 6:
        mSingle = min(single) * 6
        n -= 6
    else:
        mSingle = min(single) * n
        n -= n
    if mSingle < mPack:
        res += mSingle
    else:
        res += mPack
print(res)
