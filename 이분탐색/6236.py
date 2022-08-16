# 6236 용돈 관리
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

start = min(array)
end = sum(array)
res = 0

while start <= end:
    mid = (start + end) // 2
    balance = 0  # 잔고
    count = 0  # 인출횟수

    for today in array:  # 오늘 사용할 금액 체크
        if balance < today:
            balance = mid
            count += 1

        balance -= today  # 잔고에서 오늘 사용할 금액 빼기

    # 인출횟수가 m보다 많거나 mid가 최대 예산보다 작으면 mid값 증가시키기
    if count > m or mid < max(array):
        start = mid + 1
    else:
        end = mid - 1
        res = mid

print(res)
