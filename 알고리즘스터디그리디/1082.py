# # keep
# import sys
# sys.setrecursionlimit(10**9)
# input = sys.stdin.readline

# n = int(input())

# price = list(map(int, input().split()))

# m = int(input())

# res = [0]
# minPrice = min(price)
# minPriceN = 0

# for i in range(len(price)):
#     if price[i] == minPrice:
#         # i가 가장 작은 값을 가진 n번위의 값
#         minPriceN = i

# res[0] = minPriceN
# m -= minPrice

# # 가장 작은 값으로 살수있는것을 쭉 이어 붙이는 게임
# res += [minPriceN for _ in range(m // minPrice)]

# m += minPrice

# roomNum = []

# # 이유는 적어도 하나의 숫자를 살수있다고 했으니까
# if n == 1:
#     print(0)
#     exit(0)

# while True:
#     # 돈이 0원 or 남은 돈이 숫자를 살수있는 금액이 아님
#     if m == 0 or m < minPrice:
#         break

#     for i in range(n-1, -1, -1):
#         if m == 0 or m < minPrice:
#             break
#         if m >= price[i]:
#             m -= price[i]
#             roomNum.append(i)

# if ''.join(str(s) for s in res) <= ''.join(str(s) for s in roomNum):
#     print(''.join(str(s) for s in roomNum))
# else:
#     print(''.join(str(s) for s in res))


import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())  # 문방구에서 파는 숫자 0 ~ N-1
price = list(map(int, input().split()))  # 숫자의 가격
M = int(input())  # 숫자를 구매하기 위해 준비한 금액

res = [0]  # 방 번호를 저장해 두기 위한 리스트
minPrice = float('inf')  # 숫자의 가격 중 가장 싼 가격
minPriceNum = 0  # 가장 싼 가격을 가진 숫자

for i in range(1, N):  # 0은 맨 앞에 오지 못하므로 처음에는 1부터 체크한다.
    if price[i] <= minPrice:
        minPrice = price[i]
        minPriceNum = i

# 만약 1부터 N-1까지의 숫자 중 M원으로 살 수 있는 숫자가 없다면 0을 출력하고 종료한다.
# 문제에서 적어도 하나의 숫자를 살 수 있는 입력만 주어진다고 했으므로 1이상을 사지 못한다면 0은 무조건 살 수 있다.
if minPrice > M:
    print('0')
    sys.exit(0)

res[0] = minPriceNum  # res 리스트의 첫 번째 숫자를 설정
M -= minPrice  # M원에서 minPrice만큼 사용

if price[0] < minPrice:  # 숫자 0의 가격이 더 쌀 경우 minPrice를 갱신한다.
    minPrice = price[0]
    minPriceNum = 0

# minPriceNum을 M원으로 살 수 있는 만큼 사서 res 뒤에 붙여준다.
res += [minPriceNum for _ in range(M // minPrice)]
remain = M % minPrice  # 이렇게 숫자를 만들고 나서 남은 금액

# 먼저 첫 번째 숫자에 대해서 남은 금액을 이용하여 더 큰 숫자로 대체할 수 있는지 체크한다.
if remain != 0:
    for i in range(N-1, res[0], -1):
        if remain >= price[i] - price[res[0]]:
            remain -= (price[i] - price[res[0]])
            res[0] = i
            break

# 이제 뒤에 숫자에 대해서 남은 금액을 이용하여 더 큰 숫자로 대체할 수 있는지 체크한다.
for i in range(1, len(res)):
    if remain == 0:
        break

    for j in range(N-1, minPriceNum, -1):
        if remain >= price[j] - minPrice:
            res[i] = j
            remain -= (price[j] - minPrice)
            break

print(''.join(map(str, res)))
