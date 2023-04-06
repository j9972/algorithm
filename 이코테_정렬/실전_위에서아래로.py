import sys
input = sys.stdin.readline

arr = []
for i in range(int(input())):
    arr.append(int(input()))

res = sorted(arr, key=lambda x:-x) # res = sorted(arr, reverse=True

print(res)