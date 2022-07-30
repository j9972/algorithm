import sys
input = sys.stdin.readline

n = int(input())  # 크레인 갯수
limitWeight = list(map(int, input().split()))  # 각 크레안의 무게 제한
m = int(input())  # 박스 수
boxWeight = list(map(int, input().split()))  # 박스 무게

limitWeight.sort(reverse=True)
boxWeight.sort(reverse=True)

if limitWeight[0] < boxWeight[0]:
    print(-1)
    exit(0)

# if minLimitWeight > maxBoxWeight:
#     print((m//n) + 1)
#     exit(0)

# # 사용할 수 없는 크레인제거
# for i in limitWeight:
#     if i < minBoxWeight:
#         limitWeight.remove(i)

# 남아 있는 limitweight는 한번이라도 사용할 수 있다.

count = 0

while len(boxWeight) > 0:
    count += 1

    for i in limitWeight:
        for j in boxWeight:
            # 특정하게 분리를 하려고 하지말고 전체적으로 보는 습관을 들이기
            if i >= j:
                del j
                break

print(count)
