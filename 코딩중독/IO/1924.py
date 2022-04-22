x, y = map(int, input().split())
arr1 = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
arr2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
d = 0
for i in range(0, x-1):
    d += arr2[i]

# 전체 날들을 합쳐서 7로 나누면 됨
d = (d+y) % 7
print(arr1[d])
