import sys
input = sys.stdin.readline


arr = [True for i in range(100001)]

for i in range(2, 100001):
    if arr[i] == True:  # i가 소수
        j = 2  # j는 배수값 의미
        while i * j <= 100000:
            arr[i*j] = False
            j += 1


while True:
    testCase = int(input())
    if testCase == 0:
        break

    for i in range(3, len(arr)):
        if arr[i] and arr[testCase-i]:
            print('{} = {} + {}'.format(testCase, i, testCase-i))
            break
