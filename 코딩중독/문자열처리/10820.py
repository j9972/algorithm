import sys
input = sys.stdin.readline

while True:
    arr = input().rstrip('\n')
    counting = [0] * 4

    if not arr:
        break

    for i in range(len(arr)):
        if arr[i].islower():
            counting[0] += 1
        elif arr[i].isupper():
            counting[1] += 1
        elif arr[i].isdigit():
            counting[2] += 1
        elif arr[i].isspace():
            counting[3] += 1

    for i in range(4):
        print(counting[i], end=' ')
