n = int(input())

res = 0
plusD = []
minusD = []

for i in range(n):
    num = int(input())
    if num > 1:
        plusD.append(num)
    elif num <= 0:
        minusD.append(num)
    else:
        res += 1

plusD.sort(reverse=True)
minusD.sort()

if len(plusD) % 2 == 0:
    for i in range(0, len(plusD), 2):
        res += plusD[i] * plusD[i+1]
else:
    for i in range(0, len(plusD)-1, 2):
        res += plusD[i] * plusD[i+1]
    res += plusD[len(plusD)-1]

if len(minusD) % 2 == 0:
    for i in range(0, len(minusD), 2):
        res += minusD[i] * minusD[i+1]
else:
    for i in range(0, len(minusD)-1, 2):
        res += minusD[i] * minusD[i+1]
    res += minusD[len(minusD)-1]
print(res)
