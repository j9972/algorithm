# 성적이 낮은 순서로 학생 출력하기
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

aArr = list(map(int, input().split()))
bArr = list(map(int, input().split()))

aArr.sort()
bArr.sort(reverse=True)


for i in range(k):
    if aArr[i] >= bArr[i]:
        break
    else:
        aArr[i], bArr[i] = bArr[i], aArr[i]
print(sum(aArr))
